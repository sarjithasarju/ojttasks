import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('article.db')

# Create a cursor object to interact with the database
c = conn.cursor()

# SQL query to select all rows from the 'example' table
sql = "SELECT * FROM example"

# Execute the query and fetch all results
try:
    for row in c.execute(sql):
        print("Software: " + row[0])
        print("Version: " + str(row[1]))
        print("Price: " + str(row[2]))
        print("-" * 20)  # Separator between rows for better readability
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# Close the connection
conn.close()
