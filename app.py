from flask import Flask, jsonify, request
import pickle
import re
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

app = Flask(__name__)

# Load the Naive Bayes model
with open('naive_bayes_model.pkl', 'rb') as model_file:
    naive_bayes_model = pickle.load(model_file)

# Load CountVectorizer and TfidfTransformer
with open('count_vectorizer.pkl', 'rb') as cv_file:
    count_vectorizer = pickle.load(cv_file)

with open('tfidf_transformer.pkl', 'rb') as tfidf_file:
    tfidf_transformer = pickle.load(tfidf_file)

# Text preprocessing functions
def remove_punct(response):
    translator = str.maketrans("", "", string.punctuation)
    return response.translate(translator)

def remove_stopwords(response):
    stop = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in response.split() if word.lower() not in stop]
    return " ".join(filtered_words)

# Define route for root URL
@app.route('/')
def index():
    return 'Welcome to the Stress Detection API!'

@app.route('/predict', methods=['POST'])
def predict():
    # Get user response from request
    user_response = request.json['response']

    # Preprocess the input data
    processed_response = remove_punct(user_response)
    processed_response = remove_stopwords(processed_response)

    # Vectorize the processed response
    response_count = count_vectorizer.transform([processed_response])
    response_tfidf = tfidf_transformer.transform(response_count)

    # Make prediction
    prediction = naive_bayes_model.predict(response_tfidf)

    # Return prediction as JSON response
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
