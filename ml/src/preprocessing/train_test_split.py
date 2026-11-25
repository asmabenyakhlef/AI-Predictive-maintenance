
import pandas as pd
from pathlib import Path

# ==========================================
# 1. Project paths
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

input_path = (
    PROJECT_ROOT / "data" / "processed"
    / "step_7_6_feature_engineered.csv"
)

train_path = (
    PROJECT_ROOT / "data" / "processed"
    / "step_7_7_train.csv"
)

test_path = (
    PROJECT_ROOT / "data" / "processed"
    / "step_7_7_test.csv"
)

# ==========================================
# 2. Load dataset
# ==========================================

df = pd.read_csv(input_path)

print("Original dataset shape:", df.shape)

# ==========================================
# 3. Sort chronologically
# ==========================================

df["timestamp"] = pd.to_datetime(df["timestamp"])

df = df.sort_values("timestamp").reset_index(drop=True)

# ==========================================
# 4. Define features and target
# ==========================================

feature_columns = [
    "temperature",
    "vibration",
    "current",
    "temperature_lag_1",
    "vibration_lag_1",
    "current_lag_1",
    "temperature_rolling_mean_3",
    "temperature_rolling_std_3",
    "vibration_rolling_mean_3",
    "vibration_rolling_std_3",
    "current_rolling_mean_3",
    "current_rolling_std_3"
]

target_column = "status"

# ==========================================
# 5. Handle initial missing features
# ==========================================

print("\nMissing values before preparation:")
print(df[feature_columns].isnull().sum())

df = df.dropna(subset=feature_columns).reset_index(drop=True)

print("\nDataset after removing incomplete feature rows:")
print(df.shape)

# ==========================================
# 6. Chronological Train/Test Split
# ==========================================

split_index = int(len(df) * 0.80)

train_df = df.iloc[:split_index].copy()
test_df = df.iloc[split_index:].copy()

# ==========================================
# 7. Save datasets
# ==========================================

train_path.parent.mkdir(parents=True, exist_ok=True)

train_df.to_csv(train_path, index=False)
test_df.to_csv(test_path, index=False)

# ==========================================
# 8. Display results
# ==========================================

print("\n===================================")
print("TRAIN/TEST SPLIT COMPLETED")
print("===================================")

print("Training set:", train_df.shape)
print("Testing set:", test_df.shape)

print("\nTraining period:")
print(train_df["timestamp"].min(), "to", train_df["timestamp"].max())

print("\nTesting period:")
print(test_df["timestamp"].min(), "to", test_df["timestamp"].max())

print("\nTraining distribution:")
print(train_df[target_column].value_counts())

print("\nTesting distribution:")
print(test_df[target_column].value_counts())

print("\nTraining file:", train_path)
print("Testing file:", test_path)
