Real-World Churn Prediction Project

This project is based on predicting customer churn using real-world data from a telecom company. The idea is to eventually build a system that can simulate real-time data input, predict churn using a trained machine learning model, and display the results using a dashboard.


Day 1 - Setup

Today, I started by creating the project folder and downloading the dataset.

 Tasks Completed:
- Created the folder structure for the project
- Downloaded and added the Telco Customer Churn dataset from Kaggle
- Created this README to plan out what I’ll build over the next few days
 Dataset

-Name: Telco Customer Churn
-Source: [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
-Rows: 7,043
-Description: Includes customer demographics, account information, and whether they churned or not.


Project Plan (upcoming)

I'll build this project in parts across the next few days:

- Day 2: Data cleaning & EDA
Today I focused on understanding the dataset and preparing it for model building. This meant looking at the data types, cleaning up messy columns, and exploring how churn is related to other variables.

- Opened a new notebook: `churn_training.ipynb`
- Loaded the dataset and checked its shape, data types, and null values
- Cleaned the `TotalCharges` column and removed rows with missing data
- Dropped the `customerID` column 
- Explored churn trends using bar plots and box plots
- Churn vs Contract Type
- Churn vs Monthly Charges
- Saved my progress and committed the notebook to GitHub

- Day 3:Train logistic regression model and save
 I focused on building the actual churn prediction model using the cleaned and encoded dataset. I used logistic regression since it's a good baseline for binary classification problems like churn (yes/no).

- Selected the features (`X`) and target variable (`y`)
- Split the data into training and test sets
- Handled class imbalance using SMOTE to upsample churn cases
- Trained a logistic regression model using scikit-learn
- Evaluated the model using accuracy and classification report (got around 86% accuracy)
- Saved the trained model as `churn_model.pkl` using `joblib`
- Committed both the notebook and model file to GitHub

 
- Day 4: Simulate real-time batch input and generate prediction
Today I made the pipeline work like a real-time system using batch files.

- Wrote `simulate_data.py` to generate batch files (10 customers at a time)
- Wrote `predict_batches.py` to:
- Read each batch
- Load the trained model
- Predict churn
- Save results with a new column `PredictedChurn`
- Saved outputs into a `predictions/` folder
- Tested everything end-to-end
- Committed the batch simulation + prediction logic to GitHub

 Day 5 - Streamlit Dashboard
To wrap the project professionally, I built a live dashboard to show results.

- Created a dashboard using `Streamlit` in `dashboard.py`
- The dashboard shows:
- Latest prediction batch
- Total records, churned customers, retained customers
- A table and bar chart for easy viewing
- Hosted the dashboard online using Streamlit Cloud
- Final push to GitHub

 Live Dashboard:
[ View the Live Dashboard](https://antonawin07-streamlit-churn-dashboard.streamlit.app) ✅

 Final Project Summary

- Built a real ML pipeline with simulation, prediction, and dashboarding
- Pushed all files to GitHub with daily progress
  




