from tkinter import *


class Login:
    def __init__(self, loginwin):

        self.loginwin = loginwin
        self.loginwin.title('Log In')
        self.loginwin.geometry('350x600')


def loginWin():
    loginWin = Tk()
    Login(loginWin)
    loginWin.mainloop()


if __name__ == '__main__':
    loginWin()
