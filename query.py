import sqlite3

# Connect to the database
conn = sqlite3.connect("mlb_data.db")
cursor = conn.cursor()

print("MLB Data Query Tool")
print("Type your SQL query below. Type 'exit' to quit.\n")

while True:
    query = input("SQL> ")
    
    if query.lower() == "exit":
        break

    try:
        cursor.execute(query)
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No results.")
    
    except Exception as e:
        print(f"Error: {e}")

conn.close()
print("Connection closed.")
