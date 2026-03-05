import subprocess

print("Step 1: Collecting Metrics")
subprocess.run(["python","collect_metrics.py"])

print("Step 2: Processing Data")
subprocess.run(["python","data_processing.py"])

print("Step 3: Running AI Model")
subprocess.run(["python","anomaly_detection.py"])

print("Step 4: Checking Alerts")
subprocess.run(["python","alert_engine.py"])

print("Step 5: Self Healing Action")
subprocess.run(["python","self_healing.py"])

print("AIOps pipeline completed")