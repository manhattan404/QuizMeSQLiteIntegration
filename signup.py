from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter
from customtkinter import *
import sqlite3


class Signup:
    def __init__(self, signupWin):

        self.signupWin = signupWin
        self.signupWin.title('Sign Up')
        self.signupWin.geometry('350x600')
        self.signupWin.resizable(False, False)

        self.signupBG = Image.open('assets\\signup.png')
        bg_photo = ImageTk.PhotoImage(self.signupBG)
        self.bg = Label(self.signupWin, image=bg_photo, bg='#ffffff')
        self.bg.image = bg_photo
        self.bg.place(x=0, y=0)

        self.back_button = CTkButton(master=self.signupWin, width=80, height=25, text="Back", border_width=0, corner_radius=15,
                                     fg_color="#5F9DF7", border_color="white", text_color="white", bg_color="white", font=("Ebrima", 15))
        self.back_button.place(x=40, y=170)

        # USERNAME ENTRY
        self.user_entry = Entry(self.signupWin, width=25, fg='black', border=0,
                                bg='white', font=('Microsoft Yahei UI Light', 11))
        self.user_entry.place(x=70, y=320)
        self.user_entry.insert(0, 'Username')
        self.user_entry.bind("<FocusIn>")  # on_enter
        self.user_entry.bind("<FocusOut>")  # on_leave
        Frame(self.signupWin, width=207, height=1,
              bg='black').place(x=70, y=345)

        # PASSWORD ENTRY
        self.password_entry = Entry(self.signupWin, width=25, fg='black', border=0,
                                    bg='white', font=('Microsoft Yahei UI Light', 11))
        self.password_entry.place(x=70, y=380)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind("<FocusIn>")  # on_enter
        self.password_entry.bind("<FocusOut>")  # on_leave
        Frame(self.signupWin, width=207, height=1,
              bg='black').place(x=70, y=405)

        # CONFIRM PASSWORD
        self.confirm_entry = Entry(self.signupWin, width=25, fg='black', border=0,
                                   bg='white', font=('Microsoft Yahei UI Light', 11))
        self.confirm_entry.place(x=70, y=440)
        self.confirm_entry.insert(0, 'Confirm Password')
        self.confirm_entry.bind("<FocusIn>")  # on_enter
        self.confirm_entry.bind("<FocusOut>")  # on_leave
        Frame(self.signupWin, width=207, height=1,
              bg='black').place(x=70, y=465)


def signupWin():
    signupWin = Tk()
    Signup(signupWin)
    signupWin.mainloop()


if __name__ == '__main__':
    signupWin()
