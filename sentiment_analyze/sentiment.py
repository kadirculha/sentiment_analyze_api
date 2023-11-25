from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline



class SentimentAnalyze:
    def __init__(self):
        self.model = AutoModelForSequenceClassification.from_pretrained("models/fc369386-2a62-4610-8a34-32bd52a2ab66")
        self.tokenizer = AutoTokenizer.from_pretrained("models/fc369386-2a62-4610-8a34-32bd52a2ab66")
        self.sa = pipeline("sentiment-analysis", tokenizer=self.tokenizer, model=self.model)

    def get_sentiment_score(self, text):
        return self.sa(text)[0]["score"]

    # [{'label': 'LABEL_0', 'score': 0.9975505}]

    def get_sentiment_state(self, text):
        return self.sa(text)[0]["label"]
