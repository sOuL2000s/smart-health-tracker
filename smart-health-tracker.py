import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Sample health data (steps and sleep hours)
data = {
    "Date": pd.date_range(start="2024-10-01", periods=14, freq="D"),
    "Steps": [8000, 7500, 6800, 9000, 12000, 13000, 7000, 6000, 5000, 10000, 8500, 7300, 7800, 9000],
    "SleepHours": [7.5, 8, 6, 6.5, 8.5, 9, 7, 6.5, 6, 7, 8, 7.5, 8, 7]
}

# Create DataFrame
df = pd.DataFrame(data)

# Anomaly detection for steps
step_threshold = df["Steps"].mean() - 2 * df["Steps"].std()  # Basic outlier threshold
df["StepAnomaly"] = df["Steps"] < step_threshold

# Plot steps with anomaly indication
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Steps"], label="Steps")
plt.scatter(df[df["StepAnomaly"]]["Date"], df[df["StepAnomaly"]]["Steps"], color="red", label="Anomalies")
plt.xlabel("Date")
plt.ylabel("Steps")
plt.title("Daily Steps with Anomalies Highlighted")
plt.legend()
plt.show()

# Summary report
avg_steps = df["Steps"].mean()
avg_sleep = df["SleepHours"].mean()
print(f"Average Steps: {avg_steps:.2f}")
print(f"Average Sleep Hours: {avg_sleep:.2f}")

# Sleep pattern check
sleep_threshold = 6.5  # Minimum recommended sleep hours
df["LowSleep"] = df["SleepHours"] < sleep_threshold

# Recommendations based on sleep data
low_sleep_days = df["LowSleep"].sum()
if low_sleep_days > 3:
    print("Recommendation: Try to increase sleep hours for better health.")
else:
    print("You're maintaining a healthy sleep pattern!")

# Display summary
print("\nDaily Health Data Summary:")
print(df[["Date", "Steps", "SleepHours", "StepAnomaly", "LowSleep"]].to_string(index=False))
