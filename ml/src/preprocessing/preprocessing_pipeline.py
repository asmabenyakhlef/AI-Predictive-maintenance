# ============================================
# AI-BASED PREDICTIVE MAINTENANCE SYSTEM
# Data Preprocessing Pipeline
# ============================================

import pandas as pd
from pathlib import Path


# ============================================
# 1. PATH CONFIGURATION
# ============================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_PATH = PROJECT_ROOT / "data" / "raw" / "sensor_data.csv"


# ============================================
# 2. LOAD DATA
# ============================================

def load_data():

    print("\nLoading dataset...")

    df = pd.read_csv(DATA_PATH)

    print(f"Dataset loaded successfully: {df.shape}")

    return df


# ============================================
# 3. MISSING VALUES HANDLING
# ============================================

def handle_missing_values(df):

    print("\nChecking missing values...")

    missing_values = df.isnull().sum()

    print(missing_values)

    if missing_values.sum() == 0:

        print("No missing values detected.")

    else:

        print("Missing values detected!")

        # We stop to investigate instead of
        # automatically deleting or imputing data.

        raise ValueError("Dataset contains missing values.")

    return df


# ============================================
# 4. DUPLICATES HANDLING
# ============================================

def handle_duplicates(df):

    print("\nChecking duplicates...")

    # Detect completely duplicated rows
    duplicate_rows = df.duplicated().sum()

    print(f"Duplicate rows detected: {duplicate_rows}")

    # Remove complete duplicated rows
    df = df.drop_duplicates()

    # Convert timestamp temporarily to datetime
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    # Check duplicate timestamps
    duplicate_timestamps = df["timestamp"].duplicated().sum()

    print(f"Duplicate timestamps detected: {duplicate_timestamps}")

    # Sort data chronologically
    df = df.sort_values("timestamp")

    # Reset index
    df = df.reset_index(drop=True)

    print("Duplicate handling completed.")

    return df


# ============================================
# 5. MAIN PIPELINE
# ============================================

def main():

    print("=" * 50)
    print("DATA PREPROCESSING PIPELINE")
    print("=" * 50)

    df = load_data()

    df = handle_missing_values(df)

    df = handle_duplicates(df)

    print("\nDataset after preprocessing:")
    print(df.head())

    print("\nFinal dataset shape:", df.shape)

    print("\nPreprocessing steps completed successfully.")


# ============================================
# 6. EXECUTION
# ============================================

if __name__ == "__main__":
    main()