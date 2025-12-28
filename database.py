import sqlite3

conn = sqlite3.connect("lost_found.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS lost_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    description TEXT NOT NULL,
    contact TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
