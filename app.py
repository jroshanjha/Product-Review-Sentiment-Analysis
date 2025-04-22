from flask import Flask,render_template,jsonify,request, send_file
import pickle
import os
import joblib
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
# Vectorization technique TF-IDF or CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
import re
import streamlit as st
from logged import set_logger
import logging
logger = set_logger()
import nltk_setup
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('punkt_tab')
# stop_words = set(stopwords.words('english'))

nltk.data.path.append("/home/appuser/nltk_data")

# ✅ 1. Load the vectorizer
with open('models/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# ✅ 2. Load the trained model
with open('models/model.pkl', 'rb') as file:
    model = pickle.load(file)


# Applications 
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Main code
logger.info('Application started.')

@app.route('/')
def home():
    return render_template('index.html')    

# Preprocessing function
def preprocess(text):
    if not isinstance(text, str):
        return ''
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

# 🔍 Reusable function for prediction
def predict_sentiment(text):
    X_new = vectorizer.transform([text])

    try:
        X_new = X_new.toarray()  # For models that need dense
    except:
        pass

    prediction = model.predict(X_new)[0]
    # Predict probability
    try:
        probs = model.predict_proba(X_new)
        confidence = round(probs[0][1] * 100, 2) if prediction == 1 else round(probs[0][0] * 100, 2)
    except:
        confidence = None  # some models like SVC with no `probability=True` won't support this
        
    label = "Positive" if prediction == 1 else "Negative"
    return label , confidence

def predict_sentiment1(text):
    
    # Optional: Preprocess if needed (e.g., lowercase, remove stopwords)
    # text = preprocess(input_text)
    
    # Step 1: Vectorize
    X_new = vectorizer.transform([text])

    # Step 2: Convert to dense if needed
    try:
        X_new = X_new.toarray()
    except:
        pass  # For MultinomialNB and others that accept sparse

    # Step 3: Predict
    prediction = model.predict(X_new)[0]
    label = "Positive" if prediction == 1 else "Negative"
    return label

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text1 = request.form['review']
        text = preprocess(text1)
        prediction, confidence = predict_sentiment(text)
        # prediction = model.predict([text])[0]
        return render_template('index.html', review=text1, prediction=prediction, confidence=confidence)

@app.route('/api/',methods=['GET'])
def api():
    return 'This is an API end point.'
@app.route('/api/predict', methods=['POST'])
def api_predict():
    #data = request.get_json(force=True)
    data = request.get_json()
    # text = data.get("review", "")
    #return jsonify(data['text'])
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" in request'}), 400
    
    text = preprocess(data['text'])
    input_text = data['text']
    prediction,confidence = predict_sentiment(text)
    # prediction = model.predict([text])[0]
    return jsonify({"review": input_text, "prediction": prediction, "confidence": confidence})

   # return jsonify({'sentiment': prediction})
    # if not text:
    #     return jsonify({"error": "No review provided"}), 400

# @app.route('/api/predict', methods=['POST'])
# def api_predict():
#     data = request.get_json()

#     if not data or 'text' not in data:
#         return jsonify({'error': 'Missing "text" in request'}), 400

#     input_text = data['text']

#     # Optional: Preprocess if needed (e.g., lowercase, remove stopwords)
#     # text = preprocess(input_text)
#     text = input_text

#     # Step 1: Vectorize
#     X_new = vectorizer.transform([text])

#     # Step 2: Convert to dense if needed
#     try:
#         X_new = X_new.toarray()
#     except:
#         pass  # For MultinomialNB and others that accept sparse

#     # Step 3: Predict
#     prediction = model.predict(X_new)[0]
#     label = "Positive" if prediction == 1 else "Negative"

#     return jsonify({"review": input_text, "prediction": label})

if __name__ =='__main__':
    #logging.info("Running the main function.")
    logger.info("Running the main function.")
    # print(logging.INFO, "✅ App started successfully.")
    app.run(debug=True,port=5000,host='0.0.0.0')