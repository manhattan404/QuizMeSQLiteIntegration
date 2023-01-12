from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


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
        self.user_entry.bind("<FocusIn>", on_enter)
        self.user_entry.bind("<FocusOut>", on_leave)
        self.user_entry_frame = Frame(
            self.loginwin, width=207, height=1, bg='#111111').place(x=65, y=400)

        # PASSWORD ENTRY
        self.password_entry = Entry(self.loginwin, width=25, fg='black', border=0,
                                    bg='white', font=('Microsoft Yahei UI Light', 11))
        self.password_entry.place(x=65, y=435)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind("<FocusIn>")  # on_enter)
        self.password_entry.bind("<FocusOut>")  # on_leave)
        self.password_entry_frame = Frame(
            self.loginwin, width=207, height=1, bg='#111111').place(x=65, y=460)


def on_enter(self):
    user_entry.delete(0, 'end')


def on_leave(self):
    if self.user_entry.get() == '':
        self.user_entry.insert(0, 'Username')


def loginWin():
    loginWin = Tk()
    Login(loginWin)
    loginWin.mainloop()


if __name__ == '__main__':
    loginWin()
