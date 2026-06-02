# AutoML System
### Train • Test • Predict Automatically (Flask + Scikit-Learn)

**Live Demo:** https://automl-system-5.onrender.com

---

## Overview

A production-oriented AutoML web application that automatically preprocesses datasets, detects the machine learning task, trains multiple algorithms, selects the best-performing model, and generates predictions through an interactive web interface.

**Workflow:** Upload CSV → Train → Evaluate → Test → Predict

---

## Features

- Upload Any CSV Dataset
- Automatic Target Column Detection
- Automatic Machine Learning Task Detection (Classification / Regression)
- Automated Data Preprocessing Pipeline
- Missing Value Handling
- Feature Scaling and Encoding
- Multi-Model Training and Evaluation
- Automatic Best Model Selection
- Model Persistence using Joblib
- Dataset Testing Support
- Real-Time Predictions
- JSON API Support
- Responsive Flask Web Interface
- Cloud Deployment on Render

---

## Machine Learning Workflow

Upload Dataset

↓

Target Detection

↓

Task Detection (Classification / Regression)

↓

Data Preprocessing

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

Prediction Generation

---

## Technology Stack

### Backend

- Python
- Flask

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Joblib

### Frontend

- HTML5
- CSS3
- Bootstrap

### Deployment

- Render

---

## Supported Models

### Classification Models

- Random Forest Classifier
- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- Gradient Boosting Classifier

### Regression Models

- Random Forest Regressor
- Linear Regression
- Ridge Regression
- Decision Tree Regressor
- K-Nearest Neighbors Regressor
- Gradient Boosting Regressor
- Support Vector Regressor (SVR)

---

## Performance Metrics

### Classification

- Accuracy Score

### Regression

- R² Score

The system automatically selects the highest-performing model based on evaluation metrics.

---

## Project Structure

AutoML-Based-Multivariate-Analysis-System/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
│
├── models/
│ └── best_model.pkl
│
├── uploads/
│
├── templates/
│ ├── index.html
│ └── result.html
│
└── static/

---

## Installation

### Clone Repository

git clone https://github.com/Yash-Ghyar/AutoML-Based-Multivariate-Analysis-System.git

### Navigate to Project Directory

cd AutoML-Based-Multivariate-Analysis-System

### Install Dependencies

pip install -r requirements.txt

### Run Application

python app.py

### Open Browser

http://127.0.0.1:5000

---

## Usage

### Step 1

Upload a CSV dataset.

### Step 2

The system automatically:

- Detects the target column
- Identifies the machine learning task
- Trains multiple models
- Selects the best-performing model

### Step 3

View:

- Best Model
- Performance Score
- Task Type

### Step 4

Upload a test dataset or perform manual predictions.

---

## Project Highlights

- End-to-End Machine Learning Workflow
- Automated Model Selection
- Production-Oriented Flask Architecture
- Interactive Web Interface
- REST API Integration
- Cloud Deployment on Render
- Industry-Style ML Pipeline
- Resume-Ready AI Project

---

## Future Improvements

- Hyperparameter Tuning using GridSearchCV
- Cross Validation
- Feature Importance Visualization
- Docker Support
- Streamlit Dashboard
- Database Integration
- Authentication System

---

## Author

**Yash Ghyar**

B.Tech – Artificial Intelligence & Data Science

Vishwakarma Institute of Information Technology (VIIT), Pune

---

## Connect With Me

**GitHub**

https://github.com/Yash-Ghyar

**LinkedIn**

https://linkedin.com/in/yash-ghyar-94b58825b
