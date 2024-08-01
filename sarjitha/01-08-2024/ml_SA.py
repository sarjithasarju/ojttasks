# Data collection, preprocessing, feature extraction, training, and evaluation model
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
 
# Create a sample dataset
data = [
    ("I love NLP", "positive"),
    ("I hate this technology", "negative"),
    ("It's okay, nothing special", "neutral"),
]
 
# Separate sentences and labels
sentences, labels = zip(*data)
 
# Download the NLTK data needed
nltk.download('punkt')
nltk.download('stopwords')
 
# Initialize the stopwords
stop_words = set(stopwords.words('english'))
 
# Preprocessing function
def preprocess(text):
    # Tokenize the text and convert to lowercase
    tokens = word_tokenize(text.lower())
   
    # Remove stopwords
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
   
    # Join tokens back into a single string
    return ' '.join(filtered_tokens)
 
# Apply preprocessing to each sentence
preprocessed_sentences = [preprocess(sentence) for sentence in sentences]
 
# Feature extraction using TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_sentences)
 
# Convert labels to a list
y = list(labels)
 
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
 
# Initialize the Multinomial Naive Bayes classifier
model = MultinomialNB()
 
# Train the model
model.fit(X_train, y_train)
 
# Predict on the test set
y_pred = model.predict(X_test)
 
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
 
# Print the results
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Classification Report:{report}")