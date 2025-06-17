import sqlite3

# Connect to the working database
conn = sqlite3.connect("data/mlb.db")
cursor = conn.cursor()

# Manually add a few rows
new_rows = [
    ("Base on Balls", "Rickey Henderson", "Oakland", "98"),
    ("Base on Balls", "Eddie Murray", "Baltimore", "95"),
    ("Base on Balls", "Dwight Evans", "Boston", "93"),
    ("Base on Balls", "Reggie Jackson", "New York", "90")
]

cursor.executemany("INSERT INTO events (Statistic, Player, Team, Value) VALUES (?, ?, ?, ?);", new_rows)

conn.commit()
conn.close()
print("Sample rows added.")
