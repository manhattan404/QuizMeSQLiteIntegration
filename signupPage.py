import tkinter as tk

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

    # create the next frame
    next_frame = tk.Toplevel(window)
    next_frame.title("Next Frame")

    # add a label to the next frame
    next_frame_label = tk.Label(next_frame, text="This is the next frame")
    next_frame_label.pack()

    # close the previous frame
    window.destroy()

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
