# Use Python base image
FROM python:3.10-slim

# Set environment variable for NLTK
ENV NLTK_DATA=/app/nltk_data

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK corpora (like punkt, stopwords)
RUN python -m nltk.downloader -d /app/nltk_data punkt stopwords punkt_tab

# Expose your app port
EXPOSE 5000

# Run the app (Flask or Streamlit)
CMD ["python", "app.py"]


# # Use Python base image
# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Copy files
# COPY . .

# # Install dependencies
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

# # Download NLTK resources (punkt and stopwords)
# RUN python -m nltk.downloader punkt stopwords

# # Set environment variable to avoid runtime prompts
# ENV PYTHONUNBUFFERED=1

# # Expose Streamlit/Flask port
# EXPOSE 8501

# # Run app (change this based on your app type)
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

