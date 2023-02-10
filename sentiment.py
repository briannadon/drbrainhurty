import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_sentiment_score(message):
    msg = str(message)
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(msg)['compound']
    return score