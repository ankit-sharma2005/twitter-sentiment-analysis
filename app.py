import streamlit as st
import pickle
import pandas as pd
import re
from datetime import datetime
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Twitter Sentiment Analysis",
    page_icon="🐦",
    layout="wide"
)

# ---------------------------
# Download NLTK Data
# ---------------------------
# ---------------------------
# Download NLTK Data
# ---------------------------
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
# ---------------------------
# Load Model & Vectorizer
# ---------------------------
model = pickle.load(open("trained_model.sav", "rb"))
vectorizer = pickle.load(open("vectorizer.sav", "rb"))
# Initialize Prediction History
if "history" not in st.session_state:
    st.session_state["history"] = []

# ---------------------------
# Text Preprocessing
# ---------------------------
port_stem = PorterStemmer()

def stemming(content):
    content = re.sub('[^a-zA-Z]', ' ', str(content))
    content = content.lower()
    content = content.split()

    content = [
        port_stem.stem(word)
        for word in content
        if word not in stopwords.words('english')
    ]

    return " ".join(content)

# ---------------------------
# Prediction Function
# ---------------------------
def predict_sentiment(text):

    processed_text = stemming(text)

    vectorized_text = vectorizer.transform([processed_text])

    prediction = model.predict(vectorized_text)[0]

    try:
        confidence = max(
            model.predict_proba(vectorized_text)[0]
        )
    except:
        confidence = None

    return prediction, confidence

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("📊 Project Information")

st.sidebar.markdown("""
### Model Details

- Logistic Regression
- TF-IDF Vectorizer
- Dataset: Sentiment140
- Tweets: 1.6 Million
""")

# ---------------------------
# Main Title
# ---------------------------
st.title("🐦 Twitter Sentiment Analysis")

st.write(
    "Predict whether a tweet is Positive or Negative."
)

# ---------------------------
# ---------------------------
# Single Tweet Prediction
# ---------------------------
st.header("Single Tweet Prediction")

tweet = st.text_area(
    "Enter Tweet",
    height=150
)

if st.button("Predict Sentiment"):

    if tweet.strip() == "":
        st.warning("Please enter a tweet.")

    else:

        prediction, confidence = predict_sentiment(tweet)

        sentiment_text = (
            "Negative"
            if prediction == 0
            else "Positive"
        )

        # Save History
        st.session_state["history"].append(
            {
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Tweet": tweet,
                "Prediction": sentiment_text
            }
        )

        st.subheader("Result")

        if prediction == 0:
            st.error("😞 Negative Tweet")
        else:
            st.success("😊 Positive Tweet")

        if confidence is not None:
            st.metric(
                "Confidence",
                f"{confidence*100:.2f}%"
            )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Characters",
                len(tweet)
            )

        with col2:
            st.metric(
                "Words",
                len(tweet.split())
            )

# ---------------------------
# CSV Prediction
# ---------------------------
st.markdown("---")

st.header("📂 Batch Prediction Using CSV")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write("### Preview")

    st.dataframe(df.head())

    column_name = st.selectbox(
        "Select Tweet Column",
        df.columns
    )

    if st.button("Predict CSV"):

        predictions = []

        for text in df[column_name]:

            processed = stemming(text)

            vector = vectorizer.transform([processed])

            pred = model.predict(vector)[0]

            if pred == 0:
                predictions.append("Negative")
            else:
                predictions.append("Positive")

        df["Prediction"] = predictions

        st.success("Prediction Completed")

        st.dataframe(df.head(20))

        csv = df.to_csv(index=False)

        st.download_button(
            label="⬇ Download Results",
            data=csv,
            file_name="sentiment_predictions.csv",
            mime="text/csv"
        )
# ---------------------------
# Prediction History
# ---------------------------

st.markdown("---")

st.header("🕒 Prediction History")

if len(st.session_state["history"]) > 0:

    history_df = pd.DataFrame(
        st.session_state["history"]
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

    if st.button("🗑 Clear History"):
        st.session_state["history"] = []
        st.rerun()

else:
    st.info("No predictions yet.")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")

st.caption(
    "Built with Streamlit, Logistic Regression and TF-IDF"
)

st.markdown(
    """
    ### 👨‍💻 Developer
    
    **Ankit Sharma**
    
    Twitter Sentiment Analysis Project
    
    Developed using:
    - Python
    - Streamlit
    - Scikit-Learn
    - TF-IDF
    - Logistic Regression
    """
)

