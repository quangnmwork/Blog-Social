from transformers import AutoTokenizer
from lightning_transformers.task.nlp.text_classification import (
    TextClassificationTransformer,
)
import torch

class CFG:
    stoi = {
      "LABEL_0": 'sadness',
      "LABEL_1": 'joy',
      "LABEL_2": 'love',
      "LABEL_3": 'anger',
      "LABEL_4": 'fear',
      "LABEL_5": 'surprise',
    }
    itos = {i:s for i,s in enumerate(stoi)}

dl_model = TextClassificationTransformer(
    pretrained_model_name_or_path="prajjwal1/bert-tiny",
    num_labels=6,
    tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path="prajjwal1/bert-tiny"),
)
checkpoint = torch.load('app/torch_util/model.ckpt', map_location=torch.device('cpu'))
dl_model.load_state_dict(checkpoint['state_dict'])