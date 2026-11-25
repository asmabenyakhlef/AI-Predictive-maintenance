
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Define file paths
DATA_PATH = Path("data/raw/sensor_data.csv")
OUTPUT_DIR = Path("data/processed")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 2. Load the dataset
df = pd.read_csv(DATA_PATH)

# 3. Display basic information
print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== DATASET INFORMATION =====")
df.info()

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# 4. Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 5. Check duplicated rows
print("\n===== DUPLICATES =====")
print(df.duplicated().sum())

# 6. Analyze machine status
print("\n===== MACHINE STATUS =====")
print(df["status"].value_counts())

# 7. Calculate correlation
print("\n===== CORRELATION =====")
print(
    df[["temperature", "vibration", "current"]].corr()
)

# 8. Plot sensor distributions
df[["temperature", "vibration", "current"]].hist(
    figsize=(10, 6),
    bins=15
)

plt.suptitle("Sensor Measurements Distribution")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "sensor_distributions.png")
plt.show()

# 9. Plot normal vs anomaly
df["status"].value_counts().plot(
    kind="bar",
    title="Normal vs Anomaly Measurements"
)

plt.xlabel("Machine Status")
plt.ylabel("Number of Measurements")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "machine_status.png")
plt.show()

# 10. Plot sensor evolution over time
df["timestamp"] = pd.to_datetime(df["timestamp"])

df = df.sort_values("timestamp")

plt.figure(figsize=(12, 5))

plt.plot(df["timestamp"], df["temperature"])

plt.title("Temperature Evolution")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "temperature_evolution.png")
plt.show()

print("\nEDA COMPLETED SUCCESSFULLY!")
