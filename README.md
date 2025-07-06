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

* Opened a new notebook: `churn_training.ipynb`
* Loaded the dataset and checked its shape, data types, and null values
* Cleaned the `TotalCharges` column and removed rows with missing data
* Dropped the `customerID` column 
* Explored churn trends using bar plots and box plots
 * Churn vs Contract Type
 * Churn vs Monthly Charges
* Saved my progress and committed the notebook to GitHub

- Day 3:Train logistic regression model and save it
- Day 4: Simulate real-time batch input and generate predictions
- Day 5: Build a dashboard using Streamlit to display churn risk


Folder Structure (so far)

