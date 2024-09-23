import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('gridwatch.db')
c = conn.cursor()

c.execute("SELECT * FROM dim_energy_output_flow limit 20;")
rows = c.fetchall()

# Get column names
col_names = [description[0] for description in c.description]

# Convert to DataFrame
df_stg_power_data = pd.DataFrame(rows, columns=col_names)

# Display the DataFrame
print(df_stg_power_data)

# Commit and close the connection
conn.commit()
conn.close()