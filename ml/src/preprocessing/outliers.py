
import pandas as pd
from pathlib import Path

# ==========================================
# 1. Project paths
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

input_path = PROJECT_ROOT / "data" / "processed" / "step_7_3_no_duplicates.csv"

output_path = PROJECT_ROOT / "data" / "processed" / "step_7_4_outliers_report.csv"

# ==========================================
# 2. Load dataset
# ==========================================

df = pd.read_csv(input_path)

print("Dataset loaded successfully")
print("Dataset shape:", df.shape)

# ==========================================
# 3. Sensor columns
# ==========================================

sensor_columns = ["temperature", "vibration", "current"]

# ==========================================
# 4. Detect outliers using IQR
# ==========================================

outliers_list = []

for column in sensor_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    mask = (
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    )

    outliers = df[mask]

    print(f"\n===== {column.upper()} =====")
    print(f"Q1: {Q1:.3f}")
    print(f"Q3: {Q3:.3f}")
    print(f"IQR: {IQR:.3f}")
    print(f"Lower bound: {lower_bound:.3f}")
    print(f"Upper bound: {upper_bound:.3f}")
    print(f"Outliers detected: {len(outliers)}")

    for index, row in outliers.iterrows():

        outliers_list.append({
            "row_index": index,
            "timestamp": row["timestamp"],
            "sensor": column,
            "value": row[column],
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "status": row["status"]
        })

# ==========================================
# 5. Generate outlier report
# ==========================================

report_columns = [
    "row_index",
    "timestamp",
    "sensor",
    "value",
    "lower_bound",
    "upper_bound",
    "status"
]

outliers_df = pd.DataFrame(
    outliers_list,
    columns=report_columns
)

output_path.parent.mkdir(parents=True, exist_ok=True)

outliers_df.to_csv(output_path, index=False)

# ==========================================
# 6. Final summary
# ==========================================

print("\n===================================")
print("OUTLIER DETECTION COMPLETED")
print("===================================")

print("Total outliers detected:", len(outliers_df))

if not outliers_df.empty:
    print("\nDetected outliers:")
    print(outliers_df.to_string(index=False))
else:
    print("\nNo outliers detected.")

print("\nReport saved to:", output_path)

print("\nOriginal dataset shape:", df.shape)
print("No rows were removed.")
