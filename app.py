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

    score = sentiment_analysis.get_sentiment_score(text=text)
    state = sentiment_analysis.get_sentiment_state(text=text)

    return {
        "sentiment_state": state,
        "sentiment_score": round(score, 3)
    }


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
