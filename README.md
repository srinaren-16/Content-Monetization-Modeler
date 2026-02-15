# 📊 Content Monetization Modeler

## 🚀 Project Overview
Content Monetization Modeler is a machine learning project that predicts YouTube ad revenue using regression techniques. The model estimates `ad_revenue_usd` based on video performance metrics such as views, engagement, watch time, subscriber count, and contextual features like category, device, and country.

This project demonstrates an end-to-end data science workflow including EDA, preprocessing, feature engineering, model comparison, evaluation, and deployment using Streamlit.

---

## 🎯 Problem Statement
As creators and media companies rely heavily on YouTube for income, predicting potential ad revenue becomes essential for financial planning and content optimization.

The objective of this project is to build and evaluate multiple regression models to accurately predict YouTube ad revenue and deploy the best-performing model into an interactive web application.

---

## 📁 Dataset Information

- **Dataset Name:** YouTube Monetization Modeler  
- **Format:** CSV  
- **Rows:** ~122,000  
- **Target Variable:** `ad_revenue_usd`

### 📌 Features
- `video_id`
- `date`
- `views`
- `likes`
- `comments`
- `watch_time_minutes`
- `video_length_minutes`
- `subscribers`
- `category`
- `device`
- `country`
- `ad_revenue_usd` (Target)

---

## 🛠️ Project Workflow

### 1️⃣ Exploratory Data Analysis (EDA)
- Revenue distribution analysis
- Correlation heatmap
- Views vs Revenue relationship
- Engagement impact analysis
- Outlier detection

### 2️⃣ Data Preprocessing
- Removed duplicate records (~2%)
- Handled missing values (~5%)
- One-hot encoded categorical variables
- Scaled numerical features 

### 3️⃣ Feature Engineering
- Engagement Rate
- Watch Time Per View
- Retention Rate

### 4️⃣ Model Building
Trained and compared 5 regression models:
- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### 5️⃣ Model Evaluation
Evaluated using:
- R² Score
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)

The best-performing model was selected based on highest R² and lowest error metrics.

---

## 🏆 Results & Insights
- Views strongly influence revenue generation.
- Engagement rate amplifies monetization.
- Watch time contributes to higher ad exposure.
- Certain countries and devices generate higher ad revenue.
- Tree-based models captured non-linear relationships better than linear models.

---

## 🌐 Streamlit Application
The project includes a Streamlit app that allows users to:

- Input video performance metrics
- Predict estimated ad revenue
- View model-driven insights

---
##  Project Structure

```text
Content-Monetization-Modeler/
│
├── README.md
│
├── YouTube Ad Revenue Dataset.csv
│
├── app.py
│
├── best_model.pkl
│
└── project.py

---
 

