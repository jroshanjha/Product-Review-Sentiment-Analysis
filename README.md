# -Customer-Review-Classification

# 💬 Sentiment Analysis System – Customer Review Classification

Objective: Analyze customer reviews and classify them as positive or negative.
I have download dataset from Kaggle <br>
🧹 Data Preprocessing:
1. Removed white spaces, punctuation, and stop words to clean and normalize textual data. 

2. Handled case normalization and noise reduction for better token consistency.

# 🧠 Text Processing & Feature Engineering:
1. Utilized NLTK for tokenization, stemming, and lemmatization to reduce words to their base form.

2. Applied Bag of Words (BoW) and TF-IDF vectorization to convert text into meaningful numerical feature vectors.

# 🤖 Model Training:
1. Trained various ML models including Logistic Regression, Naive Bayes, and SVM for sentiment prediction.

2. Compared model performance using metrics such as Accuracy, Precision, Recall, and F1-score.

# 📈 Results:
1. Achieved high classification accuracy in distinguishing between positive and negative reviews.

2. Demonstrated effectiveness of feature engineering and preprocessing in improving model performance.

# 🤖 Skills: 
Python EDA , Stastics ,Data Cleaning and Preprocessing,  Supervised Learning , Product Review Sentiment Analysis , Model Building , Future engineer , Sentiment Analysis ,NLP , Predictive Modeling, Kaggle 



# Created Environment Variables & activate:-
conda create -p venv python==3.10 -y 
conda activate venv/

## Create Virtual Environments & activate:- 
python -m venv my_code
my_code/Scripts/activate


# Install required packages:-
pip install -r requirements.txt

# Testing End Points:- 
code/Scripts/activate  
python app.py

URL:- http://localhost:5000
Text:- 

"Terrible experience, I want a refund"
"text": "I really loved this product!"
"text":"this is good but Worst product ever"
"Worst product ever but this is good"
"This dog food is amazing!"

# 🧪 Testing API end points 
<!-- 🧪 How to Use the API
🧠 cURL example: -->

curl -X POST http://localhost:5000/api/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "I really loved this product!"}'


POSTMAN :- 

1. Create a new request
2. Select POST as the request method
3. Enter the URL of the API endpoint
4. Select the JSON body option
5. Enter the JSON data in the body field
6. Click the Send button to send the request
7. Check the response in the response body field
# 🚀 API Endpoints
// {
// "review":{
//   "text":"Terrible experience, I want a refund"}
  
// }

// {"text": "I really loved this product!"}


// {"text":"this is good but Worst product ever"}

// {"text": "Worst product ever but this is good"}

// {"text":"This dog food is amazing!"}


# Deployment Using Github and Docker (CI/CD Pipeline)

🧠 Explanation:
web: tells Render this is a web service.

gunicorn is a production-ready server.

app:app refers to:

The Python file name app.py (left side)

The Flask app object app inside app.py (right side)


# Procfile
web: gunicorn app:app


# ✅ Step 3: Build and run Docker locally
docker build -t jroshan/review-app .

# Docker Images
docker images

# Rund Docker App
docker run -p 5000:5000 jroshan/review-app


## docker port , host
docker psc

## push docker image into docker container
docker login ( jroshan)

docker image rm -f review-app

# rename 
docker tag jroshan/chatbot jroshan/review-app


# push 
docker push jroshan/review-app
docker push jroshan/review-app:lates

docker pull jroshan/review-app:latest

# final :- 
docker run -d -p 8080:8080 jroshan/review-app:latest

# ✅ 4. Access in Browser
http://localhost:5000
http://127.0.0.1:5000/


# ✅ Option 5: Streamlit Community Cloud
Fastest for basic apps, no Docker required.

Steps:
Push your Streamlit project to GitHub

Go to streamlit.io/cloud

Click "New App" → choose your repo

Set app.py as the entry file

Click Deploy


# Challening :- 

mkdir -p ~/.nltk_data