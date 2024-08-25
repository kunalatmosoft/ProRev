from flask import Flask, render_template, request, jsonify
from model.sentiment_model import SentimentModel

app = Flask(__name__)
sentiment_model = SentimentModel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['review']
        sentiment = sentiment_model.analyze_sentiment(text)
        return jsonify(sentiment)

if __name__ == '__main__':
    app.run(debug=True)
