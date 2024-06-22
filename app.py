from flask import Flask, request, render_template, redirect, url_for
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy

# Charger le modèle spacy pour le traitement linguistique
nlp = spacy.load("en_core_web_sm")

# Initialiser Flask
app = Flask(__name__)

def textblob_sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    if sentiment_polarity > 0:
        return "positif"
    elif sentiment_polarity < 0:
        return "négatif"
    else:
        return "neutre"

def sentiment_analysis(text):
    sia = SentimentIntensityAnalyzer()
    doc = nlp(text)
    sentiment_scores = [sia.polarity_scores(token.text)["compound"] for token in doc if token.is_alpha]
    total_tokens = len(sentiment_scores)
    positive_percentage = (sum(1 for score in sentiment_scores if score > 0) / total_tokens) * 100
    negative_percentage = (sum(1 for score in sentiment_scores if score < 0) / total_tokens) * 100
    neutral_percentage = (sum(1 for score in sentiment_scores if score == 0) / total_tokens) * 100

    sentiments = {
        "positif": positive_percentage,
        "négatif": negative_percentage,
        "neutre": neutral_percentage
    }

    dominant_sentiment = max(sentiments, key=sentiments.get)
    
    # Appel à TextBlob pour vérifier le sentiment
    textblob_sentiment = textblob_sentiment_analysis(text)

    return f"Sentiment dominant (Text analysis): {dominant_sentiment.capitalize()} ({sentiments[dominant_sentiment]:.2f}%)\n" \
           f"Sentiment (Review analysis): {textblob_sentiment.capitalize()}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    sentiment_result = ""
    if request.method == 'POST':
        text = request.form['text']
        sentiment_result = sentiment_analysis(text)
    return render_template('index.html', sentiment_result=sentiment_result)

if __name__ == '__main__':
    app.run(debug=True)
