import pandas as pd
import time
import os

df = pd.read_csv("telco_churn_data.csv")
os.makedirs("batches", exist_ok=True)

for i in range(0, len(df), 10):
    batch = df.iloc[i:i+10]
    batch.to_csv(f"batches/batch_{i}.csv", index=False)
    print(f"Saved: batch_{i}.csv")
    time.sleep(2)
