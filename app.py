import streamlit as st
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# ==============================
# CONFIG
# ==============================
st.set_page_config(
    page_title="🚨 Phishing URL Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme and cards
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #fff;
            font-family: 'Poppins', sans-serif;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1.5em;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #2ca02c;
            transform: scale(1.05);
        }
        .card {
            background: rgba(0, 0, 0, 0.5);
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        }
        .phishing {
            border-left: 6px solid #ff4c4c;
        }
        .legit {
            border-left: 6px solid #4cff4c;
        }
        .url-text {
            font-weight: bold;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# ==============================
# LOAD MODEL & TOKENIZER
# ==============================
model = tf.keras.models.load_model("models/phishing_cnn_model.h5")
with open("models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)
max_length = 200

# ==============================
# APP TITLE
# ==============================
st.title("🚨 Phishing URL Detector")
st.write("Enter one or multiple URLs to check if they are phishing or legitimate.")

# ==============================
# URL INPUT
# ==============================
urls_input = st.text_area(
    "Enter URLs (one per line)",
    placeholder="https://example.com\nhttp://another-example.com"
)

urls = [url.strip().lower().replace("https://","").replace("http://","").rstrip("/") 
        for url in urls_input.split("\n") if url.strip()]

# ==============================
# DETECT BUTTON
# ==============================
if st.button("Check URLs") and urls:
    sequences = tokenizer.texts_to_sequences(urls)
    X = pad_sequences(sequences, maxlen=max_length, padding='post')
    predictions = model.predict(X).flatten()

    threshold = 0.7

    st.markdown("---")
    st.subheader("Results:")

    for url, prob in zip(urls, predictions):
        if prob > threshold:
            status = "PHISHING ⚠️"
            card_class = "card phishing"
            color = "#ff4c4c"
        else:
            status = "LEGITIMATE ✅"
            card_class = "card legit"
            color = "#4cff4c"

        bar_width = int(prob * 100)
        st.markdown(f"""
            <div class="{card_class}">
                <div class="url-text">{url}</div>
                <div style="background: rgba(255,255,255,0.2); border-radius: 8px; width: 100%; height: 15px; margin-top: 8px;">
                    <div style="width: {bar_width}%; height: 100%; background: {color}; border-radius: 8px;"></div>
                </div>
                <div style="margin-top:5px;">Prediction Probability: {prob:.2f} → {status}</div>
            </div>
        """, unsafe_allow_html=True)

    # Optional: Save results
    import pandas as pd
    if st.checkbox("Save results to CSV"):
        df = pd.DataFrame({
            "URL": urls,
            "Probability": predictions,
            "Prediction": ["PHISHING" if p > threshold else "LEGITIMATE" for p in predictions]
        })
        df.to_csv("phishing_results.csv", index=False)
        st.success("✅ Results saved to phishing_results.csv")

else:
    st.info("Enter URLs above and click 'Check URLs' to start detection.")