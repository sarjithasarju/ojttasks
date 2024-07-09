import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('article.db')

# Create a cursor object to interact with the database
c = conn.cursor()

# Create a table named 'example'
try:
    c.execute("""
        CREATE TABLE IF NOT EXISTS example (
            Software TEXT,
            Version REAL,
            Price REAL
        )
    """)
    print("Table created successfully.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# Commit the changes and close the connection
conn.commit()
conn.close()
