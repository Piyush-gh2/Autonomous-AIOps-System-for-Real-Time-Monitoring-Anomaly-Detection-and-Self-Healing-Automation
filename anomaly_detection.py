import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("processed_metrics.csv")

model = IsolationForest(contamination=0.05)

features = df[["cpu_usage","memory_usage","cpu_memory_ratio"]]

df["anomaly"] = model.fit_predict(features)

df.to_csv("prediction_results.csv", index=False)

print(df.tail())