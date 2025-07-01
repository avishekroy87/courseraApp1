import sqlite3

conn = sqlite3.connect('/Users/avishekroy/Library/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db')
cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM Artist limit 0,10")

    rows = cursor.fetchall()
    print(f"The number of rows is:{len(rows)}")

    for i,row in enumerate(rows, 1):
        print(f"Row {i}: {row}")

except sqlite3.Error as e:
    print(f"SQLite error: {e}")
