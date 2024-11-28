from .base import BaseDataset
from datasets import load_dataset
from opencompass.registry import LOAD_DATASET
import json
from datasets import Dataset

@LOAD_DATASET.register_module()
class XCOPASDataset(BaseDataset):

    @staticmethod
    def load(path):
        dataset = Dataset.from_list([json.loads(line.strip()) for line in open(path)])
        lang = path.split("/")[-1].split('_')[0]

        def preprocess(example):
            trans = {
                'cause': {'th': 'สาเหตุ', 'vi': 'gây ra', 'id': 'menyebabkan'},
                'effect': {'th': 'ผล', 'vi': 'tác dụng', 'id': 'memengaruhi'}
            }
            example['trans_question'] = trans[example['question']][lang]

            trans = {
                'cause': {'th': 'สาเหตุคืออะไร?', 'vi': 'Nguyên nhân là gì?', 'id': 'Apa penyebabnya?'},
                'effect': {'th': 'ผลของอะไร?', 'vi': 'Tác động là gì?', 'id': 'Apa efeknya?'}
            }
            example['full_question'] = trans[example['question']][lang]

            if example['label'] == 1:
                example['answer'] = '1'
            else:
                example['answer'] = '0'
            return example

        return dataset.map(preprocess)
