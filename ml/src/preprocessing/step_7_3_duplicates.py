
import pandas as pd
from pathlib import Path

# 1. Load dataset from step 7.2
input_path = Path("data/processed/step_7_2_no_missing.csv")
output_path = Path("data/processed/step_7_3_no_duplicates.csv")

df = pd.read_csv(input_path)

print("Dataset before duplicate handling:", df.shape)

# 2. Detect duplicates
duplicates = df.duplicated().sum()

print("Number of duplicate rows:", duplicates)

# 3. Remove duplicates
df = df.drop_duplicates()

print("Dataset after duplicate handling:", df.shape)

# 4. Save cleaned dataset
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print("\nStep 7.3 completed successfully!")
print("File saved:", output_path)
