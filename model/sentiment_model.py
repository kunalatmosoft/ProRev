import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

class SentimentModel:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        return self.analyzer.polarity_scores(text)
