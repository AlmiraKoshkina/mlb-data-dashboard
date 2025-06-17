import pandas as pd
import os
import sqlite3
from bs4 import BeautifulSoup

# Load the HTML page
with open("data/page_1980.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find the table with statistics
table = soup.find("table", class_="boxed")
rows = table.find_all("tr")

data = []
current_stat = None
current_value = None

for row in rows:
    cols = row.find_all("td")
    if not cols:
        continue

    # Extract text and strip whitespace
    text = [col.get_text(strip=True) for col in cols]

    # Skip header/footer rows
    if "Statistic" in text[0] or "History" in text[0]:
        continue

    # Row with full stat info
    if len(text) == 5:
        current_stat = text[0]
        player = text[1]
        team = text[2]
        current_value = text[3]
        data.append([current_stat, player, team, current_value])

    # Row with second player (rowspan)
    elif len(text) == 2:
        player = text[0]
        team = text[1]
        data.append([current_stat, player, team, current_value])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Statistic", "Player", "Team", "Value"])

# Filter out rows where player is None (just in case)
df = df[df["Player"].notna()]

# Show result
print(df)

# Save to SQLite
conn = sqlite3.connect("data/mlb.db")
df.to_sql("events", conn, if_exists="replace", index=False)
conn.close()
