# 🔮 Predictive Analytics & AI Model Deployment 🚀

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-009688?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-FF4B4B?logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.4-F7931E?logo=scikit-learn&logoColor=white)

**Project Level:** Advanced (Level 3)  
**Domain:** Artificial Intelligence & Machine Learning  
**Institution:** Cognevance Technologies  

---

## 📑 Project Overview
This repository contains a complete, end-to-end Machine Learning pipeline designed to predict **Telco Customer Churn**. It transitions from raw data collection and advanced preprocessing to model training, evaluation, and real-world web deployment. 

The core of this project features a trained Logistic Regression model wrapped in a high-performance **FastAPI** backend, accessed via an interactive, real-time **Streamlit** web dashboard for business stakeholders.

---

## 📸 Project Showcase

### 1. Interactive Web Dashboard (Streamlit)
*This dashboard allows users to input customer profiles and receive real-time churn risk assessments with actionable AI insights.*

**Dashboard Overview & Analysis:**
![Dashboard Overview](Output/Screenshot%202026-07-11%20120755.png)

**Customer Persona & Prediction Results:**
![Dashboard Results](Output/Screenshot%202026-07-11%20120814.png)

### 2. REST API Backend (FastAPI)
*The backend API automatically scales incoming JSON data and serves predictions via a locally hosted endpoint.*

**API Documentation & Testing Interface:**
![FastAPI Backend](Output/Screenshot%202026-07-11%20120831.png)

---

## 🚀 Key Features & Pipeline Architecture
1. **Data Preprocessing:** Handled hidden missing values, one-hot encoded categorical variables, and applied `MinMaxScaler` for continuous features.
2. **Feature Engineering:** Engineered a `Total_Services` feature to extract deeper behavioral patterns.
3. **Model Selection:** Trained and evaluated Logistic Regression, Random Forest, and a Deep Learning Artificial Neural Network (ANN).
4. **Backend API:** Built a RESTful API using FastAPI to serve the pickled machine learning model and scaler.
5. **Frontend UI:** Developed a responsive Streamlit dashboard featuring built-in customer personas (VIP, Flight Risk, Budget User).

---

## 📊 Model Performance Comparison

During the evaluation phase, multiple algorithms were tested on the testing split (20%). The **Logistic Regression** model proved to be the most effective for this specific business context, particularly regarding the recall metric for churned customers.

| Model Type | Overall Accuracy | Precision (Churn) | Recall (Churn) | F1-Score (Churn) |
| :--- | :---: | :---: | :---: | :---: |
| **Logistic Regression (Deployed)** | **78.7%** | **0.62** | **0.51** | **0.56** |
| Random Forest Classifier | 78.4% | 0.62 | 0.47 | 0.54 |
| Artificial Neural Network (ANN) | 77.6% | 0.60 | 0.49 | 0.54 |

---

## 🗂️ Project Structure
```text
cognevance_PredictiveAnalytics/
├── data/               # Raw Telco Churn CSV 
├── notebooks/          # Jupyter notebooks for EDA and Model Training
├── api/                # FastAPI application
│   └── main.py         # API routing and model inference
├── dashboard/          # Streamlit application
│   └── app.py          # Frontend UI and API connection
├── models/             # Serialized model objects
│   ├── churn_model.pkl # Trained Logistic Regression model
│   └── scaler.pkl      # MinMaxScaler object
├── Output/             # UI and API screenshots for documentation
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
