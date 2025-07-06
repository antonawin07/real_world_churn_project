import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Churn Dashboard", layout="wide")

st.title("📉 Real-Time Churn Prediction Dashboard")

# Check if predictions folder exists
if not os.path.exists("predictions"):
    st.warning("Predictions folder not found.")
else:
    files = sorted([f for f in os.listdir("predictions") if f.endswith(".csv")])
    
    if not files:
        st.info("No prediction files found yet.")
    else:
        latest_file = files[-1]
        df = pd.read_csv(os.path.join("predictions", latest_file))

        st.subheader(f"Latest File: `{latest_file}`")
        st.dataframe(df)

        st.metric("Total Records", len(df))
        churned = df["PredictedChurn"].sum()
        st.metric("Predicted to Churn", int(churned))
        st.metric("Retained", int(len(df) - churned))

        st.bar_chart(df["PredictedChurn"].value_counts())
