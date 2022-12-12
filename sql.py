import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')

# Create a cursor object
cursor = conn.cursor()

# Define the SQL query
query = """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
"""

# Execute the query
cursor.execute(query)

# Save changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
