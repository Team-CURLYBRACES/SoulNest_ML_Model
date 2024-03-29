from flask import Flask, jsonify, request, Response
import pickle
import re
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

app = Flask(__name__)

# Load the Naive Bayes model
with open('app/naive_bayes_model.pkl', 'rb') as model_file:
    naive_bayes_model = pickle.load(model_file)

# Load CountVectorizer and TfidfTransformer
with open('app/count_vectorizer.pkl', 'rb') as cv_file:
    count_vectorizer = pickle.load(cv_file)

with open('app/tfidf_transformer.pkl', 'rb') as tfidf_file:
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

@app.route('/predict', methods=['GET'])
def predict():
    return 'HELOOOOOOO'
    # Get user response from request
    user_response = request.json['response']

    # Tokenize the input text into sentences
    sentences = re.split(r'[.!?]', user_response)
    
    # Initialize counters
    total_sentences = len(sentences)
    stress_count = 0
    predictions = []

    # Process each sentence
    for sentence in sentences:
        # Preprocess the input data
        processed_sentence = remove_punct(sentence)
        processed_sentence = remove_stopwords(processed_sentence)

        # Vectorize the processed sentence
        response_count = count_vectorizer.transform([processed_sentence])
        response_tfidf = tfidf_transformer.transform(response_count)

        # Make prediction for the sentence
        prediction = naive_bayes_model.predict(response_tfidf)
        predictions.append(prediction[0])

        # Update stress count
        if prediction == 'Stress':
            stress_count += 1

    # Calculate stress percentage
    stress_percentage = (stress_count / total_sentences) * 100

    # Return predictions, stress count, and stress percentage as JSON response
    return jsonify({
        'predictions': predictions,
        'stress_count': stress_count,
        'stress_percentage': stress_percentage
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",  port=8001)