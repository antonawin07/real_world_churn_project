import pandas as pd
import joblib
import os

# Load your trained churn model
model = joblib.load("churn_model.pkl.ipynb")

# Make sure the predictions folder exists
os.makedirs("predictions", exist_ok=True)

# Go through each CSV batch file in the batches folder
for file in sorted(os.listdir("batches")):
    if file.endswith(".csv"):
        # Load the batch file
        df = pd.read_csv(os.path.join("batches", file))

        # Drop customerID and clean TotalCharges
        df_clean = df.drop(columns=["customerID"], errors="ignore")
        df_clean["TotalCharges"] = pd.to_numeric(df_clean["TotalCharges"], errors="coerce")
        df_clean.dropna(inplace=True)

        # One-hot encode and align columns with model input
        df_encoded = pd.get_dummies(df_clean, drop_first=True)
        df_encoded = df_encoded.reindex(columns=model.feature_names_in_, fill_value=0)

        # Predict churn
        preds = model.predict(df_encoded)

        # Add prediction column to original data
        df["PredictedChurn"] = preds

        # Save result to predictions folder
        df.to_csv(os.path.join("predictions", f"pred_{file}"), index=False)
        print(f"Predicted: {file}")

