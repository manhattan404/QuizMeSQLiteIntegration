import tkinter as tk
from tkinter import *
import sqlite3
import customtkinter
from customtkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

grey_one = '#222222'
grey_two = '#333333'
light_black = '#111111'
black = '#000000'

root = tk.Tk()
root.title("Quiz Me by Szhes")
# root.geometry('350x600+370+160')

x = int(root.winfo_screenwidth() // 2.5)
y = int(root.winfo_screenheight() * 0.15)
root.geometry('350x600' + '+' + str(x) + '+' + str(y))


root.configure(bg=grey_one)
root.resizable(False, False)


canvas = Canvas(root, bg="black", width=350, height=600)
bg = PhotoImage(file="assets/loginbg.png")
canvas.create_image(175, 300, image=bg)
canvas.place(x=0, y=0)

conn = sqlite3


def account_signup():

    global signup_bg
    root.withdraw()

    x = int(root.winfo_screenwidth() // 2.5)
    y = int(root.winfo_screenheight() * 0.15)
    # root.geometry('350x600' + '+' + str(x) + '+' + str(y))

    top_signup = Toplevel()
    top_signup.geometry('350x600' + '+' + str(x) + '+' + str(y))
    top_signup.title("Sign Up")
    top_signup.resizable(False, False)
    signup_bg = ImageTk.PhotoImage(Image.open("assets/signup.png"))
    signup_bg_label = Label(top_signup, image=signup_bg)
    signup_bg_label.place(x=0, y=0)

    def sign_up():
        usernameVar = user_entry.get()
        passwordVar = password_entry.get()
        confirm_password = confirm_entry.get()

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

        top_signup.destroy()
        root.deiconify()

    def on_enter(e):
        user_entry.delete(0, 'end')

    def on_leave(e):
        if user_entry.get() == '':
            user_entry.insert(0, 'Username')

    user_entry = Entry(top_signup, width=25, fg='black', border=0,
                       bg='white', font=('Microsoft Yahei UI Light', 11))
    user_entry.place(x=70, y=320)
    user_entry.insert(0, 'Username')
    user_entry.bind("<FocusIn>", on_enter)
    user_entry.bind("<FocusOut>", on_leave)
    Frame(top_signup, width=207, height=1, bg=light_black).place(x=70, y=345)

    def on_enter(e):
        password_entry.delete(0, 'end')

    def on_leave(e):
        if password_entry.get() == '':
            password_entry.insert(0, 'Password')

    password_entry = Entry(top_signup, width=25, fg='black', border=0,
                           bg='white', font=('Microsoft Yahei UI Light', 11))
    password_entry.place(x=70, y=380)
    password_entry.insert(0, 'Password')
    password_entry.bind("<FocusIn>", on_enter)
    password_entry.bind("<FocusOut>", on_leave)
    Frame(top_signup, width=207, height=1, bg='black').place(x=70, y=405)

    def on_enter(e):
        confirm_entry.delete(0, 'end')

    def on_leave(e):
        if confirm_entry.get() == '':
            confirm_entry.insert(0, 'Password')

    confirm_entry = Entry(top_signup, width=25, fg='black', border=0,
                          bg='white', font=('Microsoft Yahei UI Light', 11))
    confirm_entry.place(x=70, y=440)
    confirm_entry.insert(0, 'Confirm Password')
    confirm_entry.bind("<FocusIn>", on_enter)
    confirm_entry.bind("<FocusOut>", on_leave)
    Frame(top_signup, width=207, height=1, bg='black').place(x=70, y=465)

    signup_bttn = customtkinter.CTkButton(
        master=top_signup, width=120, height=32, text="Sign Up", border_width=0, corner_radius=15, fg_color="#5F9DF7", border_color="white", text_color="white", bg_color="white", font=("Ebrima", 15), command=sign_up)
    signup_bttn.place(x=107, y=510)


def welcomeScreen():
    global welcome_bg
    root.withdraw()

    x = int(root.winfo_screenwidth() // 2.5)
    y = int(root.winfo_screenheight() * 0.15)

    top_welcome = Toplevel()
    top_welcome.geometry('350x600' + '+' + str(x) + '+' + str(y))
    top_welcome.title("Main Menu")
    top_welcome.resizable(False, False)
    top_welcome.configure(bg='black')

    welcome_bg = PhotoImage(file="assets/welcome.png")
    welcomebg_label = Label(top_welcome, image=welcome_bg)
    welcomebg_label.place(x=0, y=0)

    welcome_text = Label(top_welcome, text="Welcome ",
                         bg="white", font=("Verdana", 35))
    welcome_text.place(x=55, y=270)
    username_text = Label(top_welcome, text=username + "!",
                          bg="white", font=("Verdana", 45))
    username_text.place(x=55, y=330)


def authenticate_user():
    global username
    username = user_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, password))
    result = c.fetchone()

    if result:
        print("User authenticated!")
    else:
        print("Username or password is incorrect")

    conn.close()
    welcomeScreen()

### ---------------------------------------------------------------------------------------------------------------- ###


def on_enter(e):
    user_entry.delete(0, 'end')


def on_leave(e):
    if user_entry.get() == '':
        user_entry.insert(0, 'Username')


user_entry = Entry(root, width=25, fg='black', border=0,
                   bg='white', font=('Microsoft Yahei UI Light', 11))
user_entry.place(x=70, y=365)
user_entry.insert(0, 'Username')
user_entry.bind("<FocusIn>", on_enter)
user_entry.bind("<FocusOut>", on_leave)

Frame(root, width=207, height=1, bg=light_black).place(x=70, y=390)


### ---------------------------------------------------------------------------------------------------------------- ###


def on_enter(e):
    password_entry.delete(0, 'end')


def on_leave(e):
    if password_entry.get() == '':
        password_entry.insert(0, 'Password')


password_entry = Entry(root, width=25, fg='black', border=0,
                       bg='white', font=('Microsoft Yahei UI Light', 11))
password_entry.place(x=70, y=425)
password_entry.insert(0, 'Password')
password_entry.bind("<FocusIn>", on_enter)
password_entry.bind("<FocusOut>", on_leave)

Frame(root, width=207, height=1, bg='black').place(x=70, y=450)


### ---------------------------------------------------------------------------------------------------------------- ###

login_button = customtkinter.CTkButton(
    master=root, width=120, height=32, text="Login", border_width=0, corner_radius=15, command=authenticate_user, fg_color="#5F9DF7", border_color="white", text_color="white", bg_color="white", font=("Ebrima", 15))
login_button.place(x=107, y=480)


signup = Label(root, text="Don't have an account?", fg='black',
               bg='white', font=('Microsoft YaHei UI Light', 9))
signup.place(x=65, y=530)
sign_up = Button(root, width=6, text='Sign up', border=0,
                 bg='white', cursor='hand2', fg='#57a1f8', command=account_signup)
sign_up.place(x=200, y=530)


root.mainloop()
