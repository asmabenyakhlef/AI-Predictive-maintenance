
import pandas as pd
import numpy as np
from pathlib import Path
# ==========================================
# 1. CONFIGURATION
# ==========================================


PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_PATH = PROJECT_ROOT / "data" / "raw" / "sensor_data.csv"

print("=" * 60)
print("STEP 7.1 - DATA QUALITY ASSESSMENT")
print("=" * 60)

# ==========================================
# 2. LOAD DATASET
# ==========================================

df = pd.read_csv(DATA_PATH)

print("\n[1] DATASET INFORMATION")
print("-" * 40)

print("Dataset shape:", df.shape)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# ==========================================
# 3. COLUMN TYPES
# ==========================================

print("\n[2] COLUMN DATA TYPES")
print("-" * 40)

print(df.dtypes)

# ==========================================
# 4. MISSING VALUES
# ==========================================

print("\n[3] MISSING VALUES")
print("-" * 40)

missing = pd.DataFrame({
    "Missing_Count": df.isnull().sum(),
    "Missing_Percentage": (
        df.isnull().mean() * 100
    ).round(2)
})

print(missing)

# ==========================================
# 5. DUPLICATE ROWS
# ==========================================

print("\n[4] DUPLICATE ROWS")
print("-" * 40)

print("Duplicate rows:", df.duplicated().sum())

# ==========================================
# 6. TIMESTAMP VALIDATION
# ==========================================

print("\n[5] TIMESTAMP VALIDATION")
print("-" * 40)

timestamps = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

print("Invalid timestamps:", timestamps.isna().sum())

print("Duplicate timestamps:", timestamps.duplicated().sum())

print("Chronologically sorted:", timestamps.is_monotonic_increasing)

if timestamps.notna().sum() > 1:
    intervals = timestamps.dropna().sort_values().diff().dt.total_seconds()

    print("Minimum interval (seconds):", intervals.min())
    print("Maximum interval (seconds):", intervals.max())
    print("Average interval (seconds):", round(intervals.mean(), 3))

# ==========================================
# 7. NUMERICAL VALIDATION
# ==========================================

print("\n[6] NUMERICAL DATA VALIDATION")
print("-" * 40)

numerical_columns = ["temperature", "vibration", "current"]

for column in numerical_columns:

    values = pd.to_numeric(df[column], errors="coerce")

    invalid = values.isna().sum() - df[column].isna().sum()

    print(f"\n{column}:")
    print("Invalid numerical values:", invalid)
    print("Minimum:", values.min())
    print("Maximum:", values.max())
    print("Mean:", round(values.mean(), 3))

    print("Infinite values:", np.isinf(values).sum())

# ==========================================
# 8. STATUS VALIDATION
# ==========================================

print("\n[7] STATUS VALIDATION")
print("-" * 40)

print("Unique status values:")
print(df["status"].value_counts(dropna=False))

expected_status = ["normal", "anomaly"]

unexpected = ~df["status"].isin(expected_status)

print("\nUnexpected status values:", unexpected.sum())

# ==========================================
# 9. FINAL QUALITY SUMMARY
# ==========================================

print("\n[8] FINAL QUALITY SUMMARY")
print("=" * 60)

print("Total records:", len(df))
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Invalid timestamps:", timestamps.isna().sum())
print("Unexpected status values:", unexpected.sum())

print("\nData Quality Assessment completed.")
print("=" * 60)
