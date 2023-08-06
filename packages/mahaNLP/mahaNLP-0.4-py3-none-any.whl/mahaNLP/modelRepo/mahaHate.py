from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import pandas as pd
from ..config import paths

class HateModel:
    def __init__(self, modelName='mahahate-bert', gpu_enabled:bool = False):
        self.modelName = modelName
        self.modelRoute = paths['hate'][self.modelName]
        self.tokenizer = AutoTokenizer.from_pretrained(self.modelRoute)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.modelRoute)
        self.classifier = pipeline('text-classification',
                              model=self.model, tokenizer=self.tokenizer)

    def getPolarityScore(self, text):
        result = self.classifier(text)
        df = pd.DataFrame.from_dict(result)
        return df

    def listModels(self):
        print(" hate models: ")
        for model in paths['hate']:
            print("\t",model, ": ", paths['hate'][model])
        for task in set(paths) - {'hate'}:
            print("\n",task,"models: ")
            for model in paths[task]:
                print("\t",model, ": ", paths[task][model])
