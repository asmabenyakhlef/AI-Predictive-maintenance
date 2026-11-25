
import pandas as pd
from pathlib import Path

# ==========================================
# 1. CONFIGURATION
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

INPUT_PATH = PROJECT_ROOT / "data" / "raw" / "sensor_data.csv"

OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_PATH = OUTPUT_DIR / "step_7_2_no_missing.csv"

print("=" * 60)
print("STEP 7.2 - MISSING VALUES HANDLING")
print("=" * 60)

# ==========================================
# 2. LOAD DATASET
# ==========================================

df = pd.read_csv(INPUT_PATH)

print("\nDataset loaded successfully.")
print("Shape:", df.shape)

# ==========================================
# 3. DETECT MISSING VALUES
# ==========================================

print("\n[1] MISSING VALUES ANALYSIS")
print("-" * 40)

missing_count = df.isnull().sum()

missing_percentage = (
    df.isnull().mean() * 100
).round(2)

missing_report = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percentage": missing_percentage
})

print(missing_report)

total_missing = missing_count.sum()

print("\nTotal missing values:", total_missing)

# ==========================================
# 4. MISSING VALUES TREATMENT
# ==========================================

print("\n[2] MISSING VALUES TREATMENT")
print("-" * 40)

if total_missing == 0:

    print("No missing values detected.")
    print("No imputation is required.")
    print("Original data will be preserved.")

else:

    print("Missing values detected!")
    print("Automatic imputation is not applied.")
    print("A treatment strategy must be selected")
    print("according to the affected columns.")

    raise ValueError(
        "Missing values require investigation before continuing."
    )

# ==========================================
# 5. SAVE VALIDATED DATASET
# ==========================================

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print("\n[3] DATASET SAVED")
print("-" * 40)

print("Output file:", OUTPUT_PATH)
print("Final shape:", df.shape)

print("\nSTEP 7.2 COMPLETED SUCCESSFULLY.")
print("=" * 60)
