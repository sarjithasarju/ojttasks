import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('article.db')

# Create a cursor object to interact with the database
c = conn.cursor()

# Insert values into the 'example' table
try:
    c.execute("INSERT INTO example (Software, Version, Price) VALUES ('Python', 3.4, 100)")
    c.execute("INSERT INTO example (Software, Version, Price) VALUES ('Adobe', 10.2, 1000)")
    c.execute("INSERT INTO example (Software, Version, Price) VALUES ('Office', 16, 1000)")
    print("Values inserted successfully.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# Commit the changes and close the connection
conn.commit()
conn.close()
