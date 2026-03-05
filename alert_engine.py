import pandas as pd

df = pd.read_csv("prediction_results.csv")

anomalies = df[df["anomaly"] == -1]

if len(anomalies) > 0:
    print("ALERT: System anomaly detected!")
    print(anomalies)
else:
    print("System running normally")