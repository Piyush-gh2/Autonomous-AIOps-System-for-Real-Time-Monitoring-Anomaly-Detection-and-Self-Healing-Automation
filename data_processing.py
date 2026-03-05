import pandas as pd

df = pd.read_csv("system_metrics.csv")

# Feature engineering
df["cpu_memory_ratio"] = df["cpu_usage"] / (df["memory_usage"] + 1)

print(df.head())

df.to_csv("processed_metrics.csv", index=False)