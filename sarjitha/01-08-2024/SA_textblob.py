from textblob import TextBlob

texts = [
    "i love NLP! It is great and 1'm VERY SATISFIED",
    "This is my first experience on doing sentiment analysis, I am a little bit disappointed",
    "The NLP analysis is interesting, it is neither good nor bad"
]

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment

for text in texts:
    sentiment = analyze_sentiment(text)
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment}\n")
