import os
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense, Dropout
import pickle
import matplotlib.pyplot as plt

# ==============================
# 1. Load Updated Dataset
# ==============================

DATA_PATH = r"C:\Users\SetupGame\PhishingProject\Phishing-Website-Detection-by-Machine-Learning-Techniques\data\5.urldata_updated.csv"

df = pd.read_csv(DATA_PATH)
print("CSV loaded successfully!")

df = df[["Domain", "Label"]]
df.dropna(inplace=True)

urls = df["Domain"].astype(str)
labels = df["Label"].values

# ==============================
# 2. Tokenization (Character-Level)
# ==============================

max_vocab_size = 100
max_length = 200

tokenizer = Tokenizer(num_words=max_vocab_size, char_level=True)
tokenizer.fit_on_texts(urls)

sequences = tokenizer.texts_to_sequences(urls)
X = pad_sequences(sequences, maxlen=max_length, padding='post')

y = labels

# ==============================
# 3. Train/Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 4. Build CNN Model
# ==============================

model = Sequential([
    Embedding(input_dim=max_vocab_size, output_dim=32, input_length=max_length),
    Conv1D(filters=64, kernel_size=5, activation='relu'),
    GlobalMaxPooling1D(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.summary()

# ==============================
# 5. Train Model
# ==============================

history = model.fit(
    X_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.2
)

# ==============================
# 6. Evaluate
# ==============================

loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {accuracy:.4f}")

y_pred = (model.predict(X_test) > 0.5).astype("int32")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ==============================
# 7. Save Model
# ==============================

os.makedirs("models", exist_ok=True)
model.save("models/phishing_cnn_model.h5")
print("\nDeep Learning model saved successfully!")

# Plot accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'])
plt.show()

# Save tokenizer
with open("models/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)
print("Tokenizer saved successfully!")