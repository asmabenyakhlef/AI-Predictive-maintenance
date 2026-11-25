
import pandas as pd
from pathlib import Path

# ==========================================
# 1. Project paths
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

input_path = PROJECT_ROOT / "data" / "processed" / "step_7_3_no_duplicates.csv"

output_path = PROJECT_ROOT / "data" / "processed" / "step_7_5_converted_types.csv"

# ==========================================
# 2. Load dataset
# ==========================================

df = pd.read_csv(input_path)

print("Original data types:")
print(df.dtypes)

# ==========================================
# 3. Convert timestamp
# ==========================================

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="raise"
)

# ==========================================
# 4. Convert numerical columns
# ==========================================

numeric_columns = [
    "temperature",
    "vibration",
    "current"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="raise"
    )

# ==========================================
# 5. Convert status
# ==========================================

df["status"] = df["status"].astype("category")

# ==========================================
# 6. Verify data types
# ==========================================

print("\nConverted data types:")
print(df.dtypes)

print("\nDataset shape:", df.shape)

print("\nStatus categories:")
print(df["status"].cat.categories.tolist())

# ==========================================
# 7. Save converted dataset
# ==========================================

output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)

print("\n===================================")
print("DATA TYPE CONVERSION COMPLETED")
print("===================================")

print("File saved to:", output_path)
