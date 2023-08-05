# Copyright (c) Alibaba, Inc. and its affiliates.

import re
from typing import Any, Dict, List, Union

import numpy as np
import torch
from datasets import Dataset
from transformers.models.bert.modeling_bert import BertConfig

from modelscope.metainfo import Pipelines
from modelscope.models import Model
from modelscope.outputs import OutputKeys
from modelscope.pipelines.base import Pipeline, Tensor
from modelscope.pipelines.builder import PIPELINES
from modelscope.preprocessors import DocumentSegmentationPreprocessor
from modelscope.utils.constant import Tasks
from modelscope.utils.logger import get_logger

logger = get_logger()

__all__ = ['DocumentSegmentationPipeline']


@PIPELINES.register_module(
    Tasks.document_segmentation, module_name=Pipelines.document_segmentation)
class DocumentSegmentationPipeline(Pipeline):

    def __init__(self,
                 model: Union[Model, str],
                 preprocessor: DocumentSegmentationPreprocessor = None,
                 **kwargs):

        model = model if isinstance(model,
                                    Model) else Model.from_pretrained(model)

        self.model_dir = model.model_dir
        config = BertConfig.from_pretrained(model.model_dir, num_labels=2)

        self.document_segmentation_model = model.build_with_config(
            config=config)

        if preprocessor is None:
            preprocessor = DocumentSegmentationPreprocessor(
                self.model_dir, config)
        super().__init__(model=model, preprocessor=preprocessor, **kwargs)

        self.preprocessor = preprocessor

    def __call__(self, documents: Union[List[str], str]) -> Dict[str, Any]:
        output = self.predict(documents)
        output = self.postprocess(output)
        return output

    def predict(self, documents: Union[List[str], str]) -> Dict[str, Any]:
        pred_samples = self.cut_documents(documents)
        predict_examples = Dataset.from_dict(pred_samples)

        # Predict Feature Creation
        predict_dataset = self.preprocessor(predict_examples)
        num_examples = len(
            predict_examples[self.preprocessor.context_column_name])
        num_samples = len(
            predict_dataset[self.preprocessor.context_column_name])

        predict_dataset.pop('segment_ids')
        labels = predict_dataset.pop('labels')
        sentences = predict_dataset.pop('sentences')
        example_ids = predict_dataset.pop(
            self.preprocessor.example_id_column_name)

        with torch.no_grad():
            input = {
                key: torch.tensor(val)
                for key, val in predict_dataset.items()
            }
            predictions = self.document_segmentation_model.forward(
                **input).logits

        predictions = np.argmax(predictions, axis=2)
        assert len(sentences) == len(
            predictions), 'sample {}  infer_sample {} prediction {}'.format(
                num_samples, len(sentences), len(predictions))
        # Remove ignored index (special tokens)
        true_predictions = [
            [
                self.preprocessor.label_list[p]
                for (p, l) in zip(prediction, label) if l != -100  # noqa *
            ] for prediction, label in zip(predictions, labels)
        ]

        true_labels = [
            [
                self.preprocessor.label_list[l]
                for (p, l) in zip(prediction, label) if l != -100  # noqa *
            ] for prediction, label in zip(predictions, labels)
        ]

        # Save predictions
        out = []
        for i in range(num_examples):
            out.append({'sentences': [], 'labels': [], 'predictions': []})

        for prediction, sentence_list, label, example_id in zip(
                true_predictions, sentences, true_labels, example_ids):
            if len(label) < len(sentence_list):
                label.append('B-EOP')
                prediction.append('B-EOP')
            assert len(sentence_list) == len(prediction), '{} {}'.format(
                len(sentence_list), len(prediction))
            assert len(sentence_list) == len(label), '{} {}'.format(
                len(sentence_list), len(label))
            out[example_id]['sentences'].extend(sentence_list)
            out[example_id]['labels'].extend(label)
            out[example_id]['predictions'].extend(prediction)

        return out

    def postprocess(self, inputs: Dict[str, Tensor]) -> Dict[str, Tensor]:
        """process the prediction results

        Args:
            inputs (Dict[str, Any]): _description_

        Returns:
            Dict[str, str]: the prediction results
        """
        result = []
        list_count = len(inputs)
        for num in range(list_count):
            res = []
            for s, p in zip(inputs[num]['sentences'],
                            inputs[num]['predictions']):
                s = s.strip()
                if p == 'B-EOP':
                    s = ''.join([s, '\n\t'])
                res.append(s)

            document = ('\t' + ''.join(res))
            result.append(document)

        if list_count == 1:
            return {OutputKeys.TEXT: result[0]}
        else:
            return {OutputKeys.TEXT: result}

    def cut_documents(self, para: Union[List[str], str]):
        document_list = para
        if isinstance(para, str):
            document_list = [para]
        sentences = []
        labels = []
        example_id = []
        id = 0
        for document in document_list:
            sentence = self.cut_sentence(document)
            label = ['O'] * (len(sentence) - 1) + ['B-EOP']
            sentences.append(sentence)
            labels.append(label)
            example_id.append(id)
            id += 1

        return {
            'example_id': example_id,
            'sentences': sentences,
            'labels': labels
        }

    def cut_sentence(self, para):
        para = re.sub(r'([。！.!？\?])([^”’])', r'\1\n\2', para)  # noqa *
        para = re.sub(r'(\.{6})([^”’])', r'\1\n\2', para)  # noqa *
        para = re.sub(r'(\…{2})([^”’])', r'\1\n\2', para)  # noqa *
        para = re.sub(r'([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)  # noqa *
        para = para.rstrip()
        return [_ for _ in para.split('\n') if _]
