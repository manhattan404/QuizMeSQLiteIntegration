from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter
from customtkinter import *
import sqlite3


class Login:
    def __init__(self, loginwin):

        self.loginwin = loginwin
        self.loginwin.title('Log In')
        self.loginwin.geometry('350x600')
        self.loginwin.resizable(False, False)

        self.loginBG = Image.open('assets\\loginbg.png')
        bg_photo = ImageTk.PhotoImage(self.loginBG)
        self.bg = Label(self.loginwin, image=bg_photo, bg='#ffffff')
        self.bg.image = bg_photo
        self.bg.place(x=0, y=0)

        # USERNAME ENTRY
        self.user_entry = Entry(self.loginwin, width=25, fg='black', border=0,
                                bg='white', font=('Microsoft Yahei UI Light', 11))
        self.user_entry.place(x=65, y=375)
        self.user_entry.insert(0, 'Username')
        self.user_entry.bind("<FocusIn>", self.clear_entry)
        self.user_entry.bind("<FocusOut>", self.leave_entry)
        self.user_entry_frame = Frame(
            self.loginwin, width=207, height=1, bg='#111111').place(x=65, y=400)

        # PASSWORD ENTRY
        self.password_entry = Entry(self.loginwin, width=25, fg='black', border=0,
                                    bg='white', font=('Microsoft Yahei UI Light', 11))
        self.password_entry.place(x=65, y=435)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind("<FocusIn>", self.clear_pass)  # on_enter)
        self.password_entry.bind(
            "<FocusOut>", self.leave_password)  # on_leave)
        self.password_entry_frame = Frame(
            self.loginwin, width=207, height=1, bg='#111111').place(x=65, y=460)

        # LOG IN BUTTON
        self.login_bttn = customtkinter.CTkButton(
            master=self.loginwin, width=120, height=32, text="Login", border_width=0, corner_radius=15, fg_color="#5F9DF7", border_color="white", text_color="white", bg_color="white", font=("Ebrima", 15), command=self.authenticate)
        self.login_bttn.place(x=107, y=490)

        # SIGN UP BUTTONS
        self.signup_label = Label(self.loginwin, text="Don't have an account?", fg='black',
                                  bg='white', font=('Microsoft YaHei UI Light', 9))
        self.signup_label.place(x=65, y=535)
        self.signup_bttn = Button(self.loginwin, width=6, text='Sign up', border=0,
                                  bg='white', cursor='hand2', fg='#57a1f8')
        self.signup_bttn.place(x=200, y=535)

    def clear_entry(self, event):
        self.user_entry.delete(0, END)

    def clear_pass(self, event):
        self.password_entry.delete(0, END)

    def leave_entry(self, event):
        if self.user_entry.get() == '':
            self.user_entry.insert(0, 'Username')

    def leave_password(self, event):
        if self.password_entry.get() == '':
            self.password_entry.insert(0, 'Password')

    def authenticate(self):
        self.conn = sqlite3.connect('users.db')
        self.username = self.user_entry.get()
        self.password = self.password_entry.get()
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM users WHERE username=? AND password=?",
                       (self.username, self.password))
        result = self.c.fetchone()

        if result:
            print("User authenticated!")
        else:
            print("Username or password is incorrect")

        self.conn.commit()
        self.conn.close()


def loginWin():
    loginWin = Tk()
    Login(loginWin)
    loginWin.mainloop()


if __name__ == '__main__':
    loginWin()
