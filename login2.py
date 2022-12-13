import tkinter as tk


grey_one = '#222222'
grey_two = '#333333'
light_black = '#111111'
black = '#000000'

root = tk.Tk()
root.title("Log in 2")
root.geometry('1300x750+370+160')
root.configure(bg=grey_one)


def login():

    username = user_entry.get()
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


user_label = tk.Label(root, text="Username:")
user_entry = tk.Entry(root)


password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*")


login_button = tk.Button(root, text="Log In")
signup_button = tk.Button(root, text="Sign Up")


user_label.grid(row=0, column=0)
user_entry.grid(row=0, column=1)


password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)


login_button.grid(row=2, column=0)
signup_button.grid(row=2, column=1)


root.mainloop()
