import streamlit as st
import pickle
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import numpy as np
import logging
from logged import set_logger
import nltk_setup
# Logging
logger = set_logger()
logger.info("✅ Streamlit app started")

# NLTK Setup
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Load vectorizer & model
with open('models/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

with open('models/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Preprocessing
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

# Prediction logic
def predict_sentiment(text):
    X_new = vectorizer.transform([text])
    try:
        X_new = X_new.toarray()
    except:
        pass

    prediction = model.predict(X_new)[0]

    try:
        probs = model.predict_proba(X_new)
        confidence = round(probs[0][1] * 100, 2) if prediction == 1 else round(probs[0][0] * 100, 2)
    except:
        confidence = None

    label = "Positive" if prediction == 1 else "Negative"
    return label, confidence

# Streamlit UI
st.set_page_config(page_title="Customer Review Classifier", layout="centered")
st.title("🧠 Customer Review Sentiment Classifier")

st.markdown("Enter a review below and we'll classify it as **Positive** or **Negative**.")

text_input = st.text_area("✍️ Write your review here:")

if st.button("🔍 Classify"):
    if not text_input.strip():
        st.warning("Please enter a review.")
    else:
        clean_text = preprocess(text_input)
        label, confidence = predict_sentiment(clean_text)

        st.success(f"**Prediction:** {label}")
        if confidence:
            st.info(f"**Confidence:** {confidence}%")


