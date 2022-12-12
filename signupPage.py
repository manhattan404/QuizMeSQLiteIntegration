import tkinter as tk
import sqlite3
from tkinter import messagebox

grey_one = '#222222'
grey_two = '#333333'
light_black = '#111111'
black = '#000000'


window = tk.Tk()
window.title("Sign Up")
window.geometry('350x600+370+160')
window.configure(bg=grey_one)
window.resizable(width=False, height=False)


username_label = tk.Label(text="Username:")
username_entry = tk.Entry()
password_label = tk.Label(text="Password:")
password_entry = tk.Entry(show="*")
confirm_password_label = tk.Label(text="Confirm Password:")
confirm_password_entry = tk.Entry(show="*")


# create the sign up button
def sign_up():
    usernameVar = username_entry.get()
    passwordVar = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # make sure the passwords match
    if passwordVar != confirm_password:
        tk.messagebox.showerror("Error", "Passwords do not match")
        return

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES (:username, :password)",
              {'username': usernameVar, 'password': passwordVar})

    conn.commit()
    conn.close()

    tk.messagebox.showinfo("Success", "Sign up successful")


sign_up_button = tk.Button(text="Sign Up", command=sign_up)
sign_up_button.place(x=175, y=300, anchor='center')


# username_label.grid(row=0, column=0, sticky="E")
# username_entry.grid(row=0, column=1)
# password_label.grid(row=1, column=0, sticky="E")
# password_entry.grid(row=1, column=1)
# confirm_password_label.grid(row=2, column=0, sticky="E")
# confirm_password_entry.grid(row=2, column=1)
# sign_up_button.grid(row=3, column=1, sticky="E")


window.mainloop()
