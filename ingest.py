import sqlite3
import pandas as pd

conn = sqlite3.connect('power_data.db')
c = conn.cursor()

file_path = 'C:/Users/user/Desktop/Projects/bigpay/gridwatch.csv'
df_raw = pd.read_csv(file_path)

df_raw.columns = df_raw.columns.str.strip()

# Handling missing values
missing = df_raw.isnull().sum()
if missing.any():
    print("There are missing values in the DataFrame:")
    print(missing)
    df_raw.fillna(0, inplace=True)
    print("Missing values filled with 0.")
else:
    print("No missing values in the DataFrame.")

# Handling duplicates
duplicates = df_raw.duplicated().sum()
if duplicates > 0:
    print(f"Found {duplicates} duplicate rows.")
    df_raw = df_raw.drop_duplicates()
    print("Duplicates removed.")
else:
    print("No duplicates found.")

# Convert integer columns to float and filter out rows where demand is 0
df_raw = df_raw.astype({col: 'float64' for col in df_raw.select_dtypes('int64').columns})
df_raw = df_raw.drop(df_raw[df_raw['demand'] == 0].index)

# Convert 'timestamp' to datetime
df_raw['timestamp'] = pd.to_datetime(df_raw['timestamp'])

# Extract year, month, week, and date (date only from timestamp)
df_raw['date'] = df_raw['timestamp'].dt.date
df_raw['year'] = df_raw['timestamp'].dt.year
df_raw['month'] = df_raw['timestamp'].dt.month
df_raw['week'] = df_raw['timestamp'].dt.isocalendar().week

# Create staging table with additional columns for date, week, month, and year
c.execute("""
    CREATE TABLE IF NOT EXISTS stg_power_data (
        id INTEGER PRIMARY KEY,
        timestamp DATETIME,
        date DATE,
        week INTEGER,
        month INTEGER,
        year INTEGER,
        demand REAL,
        frequency REAL,
        coal REAL,
        nuclear REAL,
        ccgt REAL,
        wind REAL,
        pumped REAL,
        hydro REAL,
        biomass REAL,
        oil REAL,
        solar REAL,
        ocgt REAL,
        french_ict REAL,
        dutch_ict REAL,
        irish_ict REAL,
        ew_ict REAL,
        nemo REAL,
        other REAL,
        north_south REAL,
        scotland_england REAL,
        ifa2 REAL,
        intelec_ict REAL,
        nsl REAL,
        vkl_ict REAL
    )
""")

df_raw.to_sql('stg_power_data', conn, if_exists='replace', index=False)
print("Data from CSV loaded into 'stg_power_data' table.")