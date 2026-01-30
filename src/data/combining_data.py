import pandas as pd
import os

# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))
raw_folder = os.path.join(script_dir, "../../data/raw")
interim_folder = os.path.join(script_dir, "../../data/interim")
os.makedirs(interim_folder, exist_ok=True)

# List of years to combine
years = [2021, 2022, 2023, 2024]

# Load all yearly datasets
dfs = []
for year in years:
    file_path = os.path.join(raw_folder, f"df_{year}.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(
            file_path,
            sep=';',
            decimal=',',
            parse_dates=['Datum von'],
            dayfirst=True
        )
        df = df.drop_duplicates(subset=['Datum von']).sort_values('Datum von').reset_index(drop=True)
        dfs.append(df)
        print(f"Loaded df_{year}.csv: shape {df.shape}")
    else:
        print(f"Warning: File for year {year} not found at {file_path}")

# Combine all years
if dfs:
    df_all_years = pd.concat(dfs, ignore_index=True)
    df_all_years = df_all_years.drop_duplicates(subset=['Datum von']).sort_values('Datum von')

    # Save combined dataset
    output_path = os.path.join(interim_folder, "df_all_years.csv")
    df_all_years.to_csv(output_path, sep=';', decimal=',', index=False)
    print(f"Combined dataset saved to: {output_path}")
    print(f"Final shape: {df_all_years.shape}")
else:
    print("No yearly DataFrames were loaded. Check file paths.")
