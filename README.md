# 🐦 Twitter Sentiment Analysis App

A Machine Learning web application built using Streamlit that predicts whether a tweet is Positive 😊 or Negative 😞.

## 📌 Project Overview

This project uses the Sentiment140 dataset containing 1.6 million tweets to train a sentiment analysis model. The application allows users to analyze tweet sentiment in real-time and perform batch predictions using CSV files.
## 🚀 Live Demo

🔗 Streamlit App:
https://twitter-sentiment-analysis-ankit.streamlit.app

## 🚀 Features

- Single Tweet Sentiment Prediction
- Confidence Score Display
- Batch CSV Prediction
- Prediction History with Timestamp
- Download Prediction Results
- Interactive Streamlit Interface

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-Learn
- TF-IDF Vectorizer
- Logistic Regression
- Pandas
- NLTK

## 📊 Dataset

Dataset Used: Sentiment140

- 1.6 Million Tweets
- Binary Sentiment Classification
- Positive and Negative Tweets

## 📂 Project Structure

```text
Twitter-sentiment-app/
│
├── app.py
├── trained_model.sav
├── vectorizer.sav
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ankit-sharma2005/twitter-sentiment-analysis.git
```

Move into project folder:

```bash
cd twitter-sentiment-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📥 Batch CSV Input

The batch predictor accepts any CSV that contains a tweet text column. Upload
the file, select the text column in the app, then click **Predict CSV**.

Minimal input:

```csv
tweet
"I absolutely love this product, it works perfectly!"
"This is the worst service I have ever used."
```

For fresh X/Twitter research, an OpenClaw workflow can collect public posts with
[TweetClaw](https://github.com/Xquik-dev/tweetclaw), review the results, and
save only the text you want to analyze into the CSV column above. Keep account
access, paid reads, private data, and any write actions inside TweetClaw's
OpenClaw approval flow before importing reviewed text into this app.

## 🎯 Sample Predictions

### Positive Tweet

```text
I absolutely love this product, it works perfectly!
```

Prediction:

```text
Positive 😊
```

### Negative Tweet

```text
This is the worst service I have ever used.
```

Prediction:

```text
Negative 😞
```

## 👨‍💻 Developer

**Ankit Sharma**

Built with Streamlit, TF-IDF and Logistic Regression.

## ⭐ Future Improvements

- Deep Learning (LSTM/BERT)
- Sentiment Analytics Dashboard
- Word Cloud Visualization
- Multi-language Support
- Live Twitter/X Integration

## 📸 Application Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Batch CSV Prediction

![Batch Prediction](screenshots/batch_prediction.png)

### Prediction History

![Prediction History](screenshots/prediction_history.png)
