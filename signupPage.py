import tkinter as tk
import sqlite3

# create the main window
window = tk.Tk()
window.title("Sign Up")

# create the input fields for username, password, and confirm password
username_label = tk.Label(text="Username:")
username_entry = tk.Entry()
password_label = tk.Label(text="Password:")
password_entry = tk.Entry(show="*")
confirm_password_label = tk.Label(text="Confirm Password:")
confirm_password_entry = tk.Entry(show="*")

# create the sign up button
def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # make sure the passwords match
    if password != confirm_password:
        tk.messagebox.showerror("Error", "Passwords do not match")
        return

    # connect to the database
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    # insert the new user into the database
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
              (username, password))

    # commit the changes and close the connection
    conn.commit()
    conn.close()

    # show a success message
    tk.messagebox.showinfo("Success", "Sign up successful")

sign_up_button = tk.Button(text="Sign Up", command=sign_up)

# use grid layout to place the input fields and button
username_label.grid(row=0, column=0, sticky="E")
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0, sticky="E")
password_entry.grid(row=1, column=1)
confirm_password_label.grid(row=2, column=0, sticky="E")
confirm_password_entry.grid(row=2, column=1)
sign_up_button.grid(row=3, column=1, sticky="E")

# run the main event loop
window.mainloop()
