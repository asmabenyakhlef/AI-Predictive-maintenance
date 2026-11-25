
import pandas as pd
from pathlib import Path

# ==========================================
# 1. Project paths
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

input_path = (
    PROJECT_ROOT / "data" / "processed"
    / "step_7_5_converted_types.csv"
)

output_path = (
    PROJECT_ROOT / "data" / "processed"
    / "step_7_6_feature_engineered.csv"
)

# ==========================================
# 2. Load dataset
# ==========================================

df = pd.read_csv(input_path)

# Restore correct data types
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["status"] = df["status"].astype("category")

print("Original dataset shape:", df.shape)

# ==========================================
# 3. Sort data chronologically
# ==========================================

df = df.sort_values("timestamp").reset_index(drop=True)

# ==========================================
# 4. Define sensor columns
# ==========================================

sensor_columns = [
    "temperature",
    "vibration",
    "current"
]

# ==========================================
# 5. Create lag features
# ==========================================

for column in sensor_columns:

    df[f"{column}_lag_1"] = df[column].shift(1)

# ==========================================
# 6. Create rolling mean and std features
# ==========================================

for column in sensor_columns:

    previous_values = df[column].shift(1)

    df[f"{column}_rolling_mean_3"] = (
        previous_values.rolling(window=3, min_periods=1).mean()
    )

    df[f"{column}_rolling_std_3"] = (
        previous_values.rolling(window=3, min_periods=2).std()
    )

# ==========================================
# 7. Verify new features
# ==========================================

print("\nNew dataset columns:")
print(df.columns.tolist())

print("\nDataset shape after feature engineering:")
print(df.shape)

print("\nNew features preview:")
print(df.head(5).to_string(index=False))

# ==========================================
# 8. Save feature-engineered dataset
# ==========================================

output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)

print("\n===================================")
print("FEATURE ENGINEERING COMPLETED")
print("===================================")

print("Original number of columns: 5")
print("Final number of columns:", len(df.columns))
print("Number of observations:", len(df))
print("Output file:", output_path)
