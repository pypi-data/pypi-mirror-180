# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Base inference implementation updates extracts with inference results."""

import copy
from typing import Dict, Optional, Tuple, Union

import apache_beam as beam
import numpy as np
import tensorflow as tf
from tensorflow_model_analysis import constants
from tensorflow_model_analysis import types
from tensorflow_model_analysis.utils import util

from tensorflow_serving.apis import prediction_log_pb2


def get_eval_shared_model(
    model_name: str, name_to_eval_shared_model: Dict[str, types.EvalSharedModel]
) -> types.EvalSharedModel:
  """Retrieves matching eval_shared_model based on model_name."""
  if model_name in name_to_eval_shared_model:
    eval_shared_model = name_to_eval_shared_model[model_name]
  elif len(name_to_eval_shared_model) == 1 and '' in name_to_eval_shared_model:
    # Attempt to recover by checking for a common case where the model_name is
    # cleared when only one value is present.
    eval_shared_model = name_to_eval_shared_model['']
  else:
    raise ValueError('ModelSpec.name should match EvalSharedModel.model_name.')
  return eval_shared_model


def _create_inference_input_tuple(
    extracts: types.Extracts) -> Tuple[types.Extracts, bytes]:
  """Creates a tuple containing the Extracts and input to the model."""
  try:
    # Note after split_extracts splits the Extracts batch, INPUT_KEY has a value
    # that is a 0 dimensional np.array. These arrays are indexed using the [()]
    # syntax.
    model_input = extracts[constants.INPUT_KEY][()]
  except KeyError as e:
    raise ValueError(
        f'Extracts must contain the input keyed by "{constants.INPUT_KEY}" for '
        'inference.') from e
  if not isinstance(model_input, bytes):
    raise ValueError(
        f'Extracts value at key: "{constants.INPUT_KEY}" is not of '
        'type bytes. Only serialized tf.Examples and serialized '
        'tf.SequenceExamples are currently supported. The value '
        f'is {model_input} and type {type(model_input)}.')
  return (extracts, model_input)


def _parse_prediction_log_to_tensor_value(
    prediction_log: prediction_log_pb2.PredictionLog
) -> Union[np.ndarray, Dict[str, np.ndarray]]:
  """Parses the model inference values from a PredictionLog.

  Args:
    prediction_log: Prediction_log_pb2.PredictionLog containing inference
      results.

  Returns:
    Values parsed from the PredictionLog inference result. These values are
    formated in the format expected in TFMA PREDICTION_KEY Extracts value.
  """
  log_type = prediction_log.WhichOneof('log_type')
  if log_type == 'classify_log':
    assert len(
        prediction_log.classify_log.response.result.classifications) == 1, (
            'We expecth the number of classifications per PredictionLog to be '
            'one because TFX-BSL RunInference expects single input/output and '
            'handles batching entirely internally.')
    classes = np.array([
        c.label for c in
        prediction_log.classify_log.response.result.classifications[0].classes
    ],
                       dtype=object)
    scores = np.array([
        c.score for c in
        prediction_log.classify_log.response.result.classifications[0].classes
    ],
                      dtype=np.float32)
    return {'classes': classes, 'scores': scores}
  elif log_type == 'regress_log':
    return np.array([
        regression.value
        for regression in prediction_log.regress_log.response.result.regressions
    ],
                    dtype=float)
  elif log_type == 'predict_log':
    return {
        k: np.squeeze(tf.make_ndarray(v), axis=0)
        for k, v in prediction_log.predict_log.response.outputs.items()
    }
  elif log_type == 'multi_inference_log':
    raise NotImplementedError(
        'MultiInferenceLog processing not implemented yet.')
  elif log_type == 'session_log':
    raise ValueError('SessionLog processing is not supported.')
  else:
    raise NotImplementedError(f'Unsupported log_type: {log_type}')


def _insert_predictions_into_extracts(
    inference_tuple: Tuple[types.Extracts,
                           Dict[str, prediction_log_pb2.PredictionLog]]
) -> types.Extracts:
  """Inserts tensor values from PredictionLogs into the Extracts.

  Args:
    inference_tuple: This is the output of inference. It includes the key
      forwarded extracts and a dict of model name to predicition logs.

  Returns:
    Extracts with the PREDICTIONS_KEY populated. Note: By convention,
    PREDICTIONS_KEY will point to a dictionary if there are multiple
    prediction logs and a single value if there is only one prediction log.
  """
  extracts = copy.copy(inference_tuple[0])
  model_names_to_prediction_logs = inference_tuple[1]
  model_name_to_tensors = {
      name: _parse_prediction_log_to_tensor_value(log)
      for name, log in model_names_to_prediction_logs.items()
  }
  if len(model_name_to_tensors) == 1:
    extracts[constants.PREDICTIONS_KEY] = list(
        model_name_to_tensors.values())[0]
  else:
    extracts[constants.PREDICTIONS_KEY] = model_name_to_tensors
  return extracts


@beam.ptransform_fn
@beam.typehints.with_input_types(types.Extracts)
@beam.typehints.with_output_types(types.Extracts)
def RunInference(extracts: beam.pvalue.PCollection,  # pylint: disable=invalid-name
                 inference_ptransform: beam.PTransform,
                 batch_size: Optional[int] = None) -> beam.pvalue.PCollection:
  """A PTransform that adds predictions and possibly other tensors to Extracts.

  Args:
    extracts: PCollection of Extracts containing model inputs keyed by
      tfma.FEATURES_KEY (if model inputs are named) or tfma.INPUTS_KEY (if model
      takes raw tf.Examples as input).
    inference_ptransform: Bulk inference ptransform used to generate
      predictions. This allows users to use different implementations depending
      on evironment or Beam runner (e.g. a cloud-friendly OSS implementation or
      an internal-specific implementation). These implementations should accept
      a pcollection consisting of tuples containing a key and a single example.
      The key may be anything and the example may be a tf.Example or serialized
      tf.Example.
    batch_size: Sets a static output batch size.

  Returns:
    PCollection of Extracts updated with the predictions.
  """
  extracts = (
      extracts
      # Extracts are fed in pre-batched, but BulkInference has specific
      # batch handling and batching requirements. To accomodate the API and
      # encapsulate the inference batching logic, we unbatch here. This function
      # returns new Extracts dicts and will not modify the input Extracts.
      | 'SplitExtracts' >> beam.FlatMap(
          util.split_extracts, expand_zero_dims=False)
      # The BulkInference API allows for key forwarding. To avoid a join
      # after running inference, we forward the unbatched Extracts as a key.
      | 'CreateInferenceInputTuple' >> beam.Map(_create_inference_input_tuple)
      | 'RunInferencePerModel' >> inference_ptransform
      # Combine predictions back into the original Extracts.
      | 'InsertPredictionsIntoExtracts' >>
      beam.Map(_insert_predictions_into_extracts))
  # Beam batch will group single Extracts into a batch. Then
  # merge_extracts will flatten the batch into a single "batched"
  # extract.
  if batch_size is not None:
    batch_kwargs = {'min_batch_size': batch_size, 'max_batch_size': batch_size}
  else:
    # Default batch parameters.
    batch_kwargs = {}
  return (extracts
          | 'BatchSingleExampleExtracts' >> beam.BatchElements(**batch_kwargs)
          | 'MergeExtracts' >> beam.Map(
              util.merge_extracts, squeeze_two_dim_vector=False))
