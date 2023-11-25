from fastapi import FastAPI, HTTPException
import uvicorn

from sentiment_analyze.sentiment import SentimentAnalyze

app = FastAPI()
sentiment_analysis = SentimentAnalyze()


@app.get('/analyze_sentiment')
def get_sentiment(text: str):
    """
   Lütfen Sentiment analizi yapılacak olan metni giriniz


   :param text:
   :return:
   """
    print(text)
    state = sentiment_analysis.get_sentiment_state(text=text)
    return {
        "sentence": text,
        "sentiment_state": state}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
