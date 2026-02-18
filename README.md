n
# Phishing URL Detection using Machine Learning & Deep Learning

**Phishing URL Detection** is a project that identifies malicious websites using a combination of **Machine Learning (ML)** and **Deep Learning (DL)** techniques. It also comes with a **user-friendly web application** built with **Streamlit** for real-time URL analysis.

---

## 🚀 Features

- Detects phishing websites using **Deep Learning (CNN)**.
- Detects phishing websites using **Machine Learning (XGBoost)**.
- Simple **command-line interface** to test URLs.
- Interactive **web application** with real-time predictions.
- Supports batch URL testing via file input.
- Displays probability of phishing and prediction status.
- Includes **visualizations** of model accuracy.

---

## 🛠️ Project Structure

Phishing-URL-Detection/
│
├── data/                   # Dataset files (legitimate & phishing URLs)
├── models/                 # Trained models and tokenizer
├── screenshot/             # Screenshots for README
├── src/                    # Scripts (training, prediction, feature extraction)
├── templates/              # Web app templates
├── app.py                  # Streamlit web app
├── README.md               # Project description and instructions
├── requirements.txt        # Python dependencies
└── predictions.csv         # Sample output of predictions

````

---

## 📊 Model Performance

### Deep Learning (CNN)

![Model Accuracy](screenshot/Figure_1.png)  
*Model accuracy over training and validation sets.*

### Machine Learning (XGBoost)

- Achieves high precision and recall on the dataset.
- Fast and lightweight for batch predictions.

---

## 💻 Example Usage

### Terminal / Command-Line

python src/predict.py https://example.com

**Output Example:**

![Terminal Results](screenshot/WhatsApp Image 2026-02-18 at 21.25.39.jpeg)

---

### Web Application

Run the app using Streamlit:

streamlit run app.py

**Web Interface:**

![Web App Results](screenshot/WhatsApp Image 2026-02-18 at 19.54.44.jpeg)

* Enter URLs to check for phishing.
* Shows **phishing probability** and **prediction**.
* Uses **colors** and **icons** for easy understanding.

---

## ⚙️ Installation

1. Clone the repository:

git clone https://github.com/yourusername/Phishing-URL-Detection-using-Machine-Learning-Deep-Learning.git
cd Phishing-URL-Detection-using-Machine-Learning-Deep-Learning

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit web app:

```bash
streamlit run app.py
```

---

## 📁 Datasets

* `data/urldata_updated.csv`: Combined dataset of legitimate and phishing URLs.
* `data/5.urldata.csv`: Original dataset.
* Additional CSVs used for training ML/DL models.

---

## ⚡ Notes

* Threshold for phishing detection in DL model is adjustable.
* Both ML and DL models can be extended to new datasets.
* The project demonstrates **practical applications of AI in cybersecurity**.

---

## 📸 Screenshots

1. Model Accuracy: `screenshot/Figure_1.png`
2. Terminal Prediction Results: `screenshot/WhatsApp Image 2026-02-18 at 21.25.39.jpeg`
3. Web App Prediction Results: `screenshot/WhatsApp Image 2026-02-18 at 19.54.44.jpeg`
4. Additional Figures: `screenshot/Figure_3.png`

```

---

If you want, I can **also suggest some nice visual touches** for the README:  

- Badges for Python version, Streamlit, ML/DL.  
- A color-coded table for prediction examples.  
- Maybe even GIFs of the web app in action.  

Do you want me to do that next?
```
