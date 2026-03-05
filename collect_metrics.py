import psutil
import time
import pandas as pd

data = []

for i in range(100):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    
    data.append({
        "cpu_usage": cpu,
        "memory_usage": memory
    })
    
df = pd.DataFrame(data)
df.to_csv("system_metrics.csv", index=False)

print("Metrics collected successfully")