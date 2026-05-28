# 🤖 AutoML-Based Multivariate Analysis System

### Train • Test • Predict — Automatically (Flask + Scikit-Learn)

🚀 **Live Demo:** [Paste Your Render Deployment Link]

---

## 📌 Overview

A production-style AutoML web application that automatically preprocesses datasets, detects the machine learning task, trains multiple algorithms, selects the best-performing model, and generates predictions through an interactive web interface.

Upload a CSV → Train → Evaluate → Test → Predict

---

# 🚀 Live Features

✅ Upload Any CSV Dataset
✅ Automatic Target Column Detection
✅ Automatic ML Task Detection (Classification / Regression)
✅ Automatic Data Preprocessing Pipeline
✅ Missing Value Handling
✅ Feature Scaling & Encoding
✅ Multi-Model Training & Evaluation
✅ Automatic Best Model Selection
✅ Model Persistence using Joblib
✅ Dataset Testing Support
✅ Real-Time Predictions
✅ JSON API Support
✅ Responsive Flask Web Interface
✅ Deployed on Render

---

# 🧠 Machine Learning Workflow

```text
Upload Dataset
      ↓
Target Detection
      ↓
Task Detection
(Classification / Regression)
      ↓
Preprocessing
(Missing Values + Encoding + Scaling)
      ↓
Train Multiple Models
      ↓
Performance Evaluation
      ↓
Best Model Selection
      ↓
Model Saving
      ↓
Prediction
```

---

# 🛠 Tech Stack

## 🔹 Backend

* Python
* Flask

## 🔹 Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

## 🔹 Frontend

* HTML
* CSS
* Bootstrap

## 🔹 Deployment

* Render

---

# ⚙️ Supported Models

## 📌 Classification Models

* Random Forest Classifier
* Logistic Regression
* Support Vector Machine (SVM)
* Decision Tree Classifier
* K-Nearest Neighbors (KNN)
* Gradient Boosting Classifier

---

## 📌 Regression Models

* Random Forest Regressor
* Linear Regression
* Ridge Regression
* Decision Tree Regressor
* K-Nearest Neighbors Regressor
* Gradient Boosting Regressor
* Support Vector Regressor (SVR)

---

# 📊 Performance Metrics

## 🔹 Classification

* Accuracy Score

## 🔹 Regression

* R² Score

The application automatically selects the highest-performing model.

---

# 📂 Project Structure

```bash
AutoML-Based-Multivariate-Analysis-System/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
│
├── models/
│   └── best_model.pkl
│
├── uploads/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│
└── screenshots/
```

---

# 💻 Installation

## Clone Repository

```bash
git clone https://github.com/Yash-Ghyar/AutoML-Based-Multivariate-Analysis-System.git
```

---

## Move to Project Directory

```bash
cd AutoML-Based-Multivariate-Analysis-System
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

---

## Open Browser

```bash
http://127.0.0.1:5000
```

---

# 📌 Usage

## Step 1

Upload CSV Dataset

---

## Step 2

System Automatically:

* Detects Target Column
* Detects ML Task
* Trains Multiple Models
* Selects Best Model

---

## Step 3

View:

* Best Model
* Performance Score
* Task Type

---

## Step 4

Upload Test Dataset or Predict Manually

---

# 🔌 API Example

## Endpoint

```bash
POST /predict_json
```

---

## Request

```json
{
  "age": 22,
  "salary": 55000,
  "experience": 2
}
```

---

## Response

```json
{
  "prediction": "Accepted"
}
```

---

# 🌟 Project Highlights

✅ End-to-End Machine Learning Workflow
✅ Automated Model Selection
✅ Production-Oriented Flask Architecture
✅ Interactive Web Interface
✅ REST API Integration
✅ Cloud Deployment on Render
✅ Industry-Level ML Pipeline
✅ Resume-Ready Full Stack AI Project

---

# 📈 Future Improvements

* Hyperparameter Tuning using GridSearchCV
* Cross Validation
* Feature Importance Visualization
* Docker Support
* Streamlit Dashboard
* Database Integration
* Authentication System

---

# 👨‍💻 Author

## Yash Ghyar

🎓 Artificial Intelligence & Data Science
🏫 Vishwakarma Institute of Information Technology (VIIT), Pune

---

# 🔗 Connect With Me

## GitHub

https://github.com/Yash-Ghyar

## LinkedIn

Paste Your LinkedIn URL

---
