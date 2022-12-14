# Import the sqlite3 module
import sqlite3

# Function to create a new database for a user


def create_user_db(username):
    # Create the database file for the user
    conn = sqlite3.connect(username + '.db')
    # Create a table for the user's data
    c = conn.cursor()
    c.execute('CREATE TABLE user_data (data1, data2, data3)')
    # Save the changes to the database
    conn.commit()
    # Close the connection to the database
    conn.close()

# Function to add data to a user's database


def add_data_to_user_db(username, data):
    # Connect to the user's database
    conn = sqlite3.connect(username + '.db')
    # Add the data to the user's table
    c = conn.cursor()
    c.execute('INSERT INTO user_data VALUES (?, ?, ?)', data)
    # Save the changes to the database
    conn.commit()
    # Close the connection to the database
    conn.close()
