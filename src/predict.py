import os
import sys
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from prettytable import PrettyTable
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# ==============================
# Paths (absolute for safety)
# ==============================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # folder of predict.py
MODEL_PATH = os.path.join(SCRIPT_DIR, "..", "models", "phishing_cnn_model.h5")
TOKENIZER_PATH = os.path.join(SCRIPT_DIR, "..", "models", "tokenizer.pkl")

# ==============================
# Load Model and Tokenizer
# ==============================
model = tf.keras.models.load_model(MODEL_PATH)

with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

max_length = 200

# ==============================
# Get URLs from Command Line or File
# ==============================
if len(sys.argv) < 2:
    print("Usage: python src/predict.py <URL1> <URL2> ... OR python src/predict.py -f urls.txt")
    sys.exit(1)

urls = []

# Check if using file input
if sys.argv[1] == "-f":
    try:
        with open(sys.argv[2], "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
else:
    urls = sys.argv[1:]

# ==============================
# Normalize URLs
# ==============================
urls = [url.lower().replace("https://", "").replace("http://", "").rstrip("/") for url in urls]

# ==============================
# Preprocess URLs
# ==============================
sequences = tokenizer.texts_to_sequences(urls)
X = pad_sequences(sequences, maxlen=max_length, padding='post')

# ==============================
# Predict
# ==============================
predictions = model.predict(X).flatten()

# ==============================
# Display Results in Table
# ==============================
threshold = 0.7  # Adjustable threshold for phishing
table = PrettyTable()
table.field_names = ["URL", "Phishing Probability", "Prediction"]

for url, prob in zip(urls, predictions):
    pred_text = Fore.RED + "PHISHING ⚠️" if prob > threshold else Fore.GREEN + "LEGITIMATE ✅"
    table.add_row([url, f"{prob:.4f}", pred_text])

print("\n===== Phishing Detection Results =====")
print(table)

# ==============================
# Optional: Save to CSV
# ==============================
save_csv = input("\nDo you want to save results to 'predictions.csv'? (y/n): ").lower()
if save_csv == "y":
    import pandas as pd
    df = pd.DataFrame({
        "URL": urls,
        "Phishing_Probability": predictions,
        "Prediction": ["PHISHING" if p > threshold else "LEGITIMATE" for p in predictions]
    })
    df.to_csv(os.path.join(SCRIPT_DIR, "..", "predictions.csv"), index=False)
    print("Results saved to predictions.csv")