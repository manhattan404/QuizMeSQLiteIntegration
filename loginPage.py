import tkinter as tk
from tkinter import *
import sqlite3
import customtkinter
from customtkinter import *
from PIL import ImageTk, Image

grey_one = '#222222'
grey_two = '#333333'
light_black = '#111111'
black = '#000000'

root = tk.Tk()
root.title("Quiz Me by Szhes")
root.geometry('350x600+370+160')
root.configure(bg=grey_one)
root.resizable(False, False)

canvas = Canvas(root, bg="black", width=350, height=600)
bg = PhotoImage(file="assets/loginbg.png")
canvas.create_image(175, 300, image=bg)
canvas.place(x=0, y=0)


conn = sqlite3


def authenticate_user():

    username = user_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, password))
    result = c.fetchone()

    if result:
        print("User authenticated!")

        root.destroy()

        mainwindow = tk.Tk()
        mainwindow.geometry('100x100+300+300')

    else:
        print("Username or password is incorrect")

    conn.close()

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
    master=root, text="Login", width=120, height=32, border_width=0, corner_radius=8, command=authenticate_user, fg_color="#5F9DF7", border_color="white", text_color="black", bg_color="white", font=("Microsoft Yahei UI Light", 15))
login_button.place(x=107, y=480)

# signup_button = customtkinter.CTkButton(
#     master=root, text="Create an account", width=120, height=15, fg_color="transparent", border_color="white", text_color="black", bg_color="white", font=("Microsoft Yahei UI Light", 13), hover=True, text_color_disabled="blue", hover_color="grey")
# signup_button.place(x=104, y=530)


signup = Label(root, text="Don't have an account?", fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 9))
signup.place(x=65, y=530)

sign_up = Button(root, width=6, text='Sign up', border=0,
                 bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=200, y=530)

root.mainloop()
