import sqlite3
import pandas as pd
import os

db_path = "mlb_data.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    year INTEGER,
    event TEXT
)
""")
conn.commit()

data_folder = "data"

for filename in os.listdir(data_folder):
    if filename.startswith("events_") and filename.endswith(".csv"):
        filepath = os.path.join(data_folder, filename)
        print(f"Importing {filename}...")
        df = pd.read_csv(filepath)
        df.to_sql("events", conn, if_exists="append", index=False)

print("Import completed.")
conn.close()
