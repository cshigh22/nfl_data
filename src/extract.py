import nfl_data_py as nfl
import pandas as pd
import os
from datetime import datetime

# 1. SETUP: Define where we want to save the data
# This gets the absolute path to your 'data/raw' folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')

# Ensure the directory exists (good practice for automation scripts)
os.makedirs(DATA_DIR, exist_ok=True)

# 2. CONFIG: Set the season we want
# Logic: If we are in Jan/Feb, we usually want the season that just finished

# We are hardcoding 2024 for now to ensure data availability
current_year = 2024

print(f"--- Starting Extraction for NFL Season {current_year} ---")

# 3. EXTRACT: Get the data from nfl_data_py
# This simulates hitting an external API endpoint
print("Fetching weekly stats...")
weekly_df = nfl.import_weekly_data([current_year])

print("Fetching roster data...")
roster_df = nfl.import_seasonal_rosters([current_year])

# 4. LOAD: Save to local CSV (Staging Area)
# We add a timestamp so we don't overwrite previous runs (useful for debugging)
timestamp = datetime.now().strftime("%Y%m%d")

weekly_filename = f"weekly_stats_{current_year}_{timestamp}.csv"
roster_filename = f"roster_{current_year}_{timestamp}.csv"

weekly_path = os.path.join(DATA_DIR, weekly_filename)
roster_path = os.path.join(DATA_DIR, roster_filename)

weekly_df.to_csv(weekly_path, index=False)
roster_df.to_csv(roster_path, index=False)

print("SUCCESS: Data saved to:")
print(f" -> {weekly_path}")
print(f" -> {roster_path}")