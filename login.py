# Import the necessary libraries
from tkinter import *
import getpass

# Create a function to handle the login process
def login():
    # Retrieve the username and password from the entry fields
    username = username_entry.get()
    password = password_entry.get()

    # Define a dictionary to store the user's credentials
    users = {
        "user1": "password1",
        "user2": "password2",
    }

    # Check if the username exists in the users dictionary
    if username in users:
        # Check if the password is correct
        if password == users[username]:
            print("Login successful!")
        else:
            print("Incorrect password, please try again.")
    else:
        print("Username not found, please try again.")

# Create a tkinter window
window = Tk()

# Create the entry fields for the username and password
username_entry = Entry(window)
password_entry = Entry(window, show="*")

# Create the login button
login_button = Button(window, text="Login", command=login)

# Place the entry fields and login button on the window
username_entry.pack()
password_entry.pack()
login_button.pack()

# Run the tkinter event loop
window.mainloop()

