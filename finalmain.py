from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import time


class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title('Quiz Me')
        self.window.geometry('1366x768+370+160')
        # self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        # window Icon
        # icon = PhotoImage(file='assets\pic-icon.png')
        # self.window.iconphoto(True, icon)

        # ======================================  HEADER ================================================= #
        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=0, width=1070, height=60)

        self.logout_text = Button(self.header, text='Logout', bg='#32cf8e', font=(
            '', 13, 'bold'), bd=0, fg='white', cursor='hand2', activebackground='#32cf8e')
        self.logout_text.place(x=950, y=15)

        # ======================================  SIDEBAR ================================================ #
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # ======================================  SIDEBAR ================================================ #
        self.heading = Label(self.header, text='Dashboard', font=(
            '', 13, 'bold'), fg='#0064d3', bg='#eff5f6')
        self.heading.place(x=325, y=70)

        # ======================================  USER AVATAR ============================================ #
        self.logoImage = Image.open('assets\\avatar.png')
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo, bg='#ffffff')
        self.logo.image = photo
        self.logo.place(x=55, y=80)

        # DASHBOARD
        self.dashboardImage = Image.open('assets\\dashboard-icon.png')
        photo = ImageTk.PhotoImage(self.dashboardImage)
        self.dashboard = Label(self.sidebar, image=photo, bg='#ffffff')
        self.dashboard.image = photo
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text='Dashboard', bg='#ffffff', font=(
            '', 13, 'bold'), bd=0, cursor='hand2', activebackground='#ffffff')
        self.dashboard_text.place(x=80, y=291)

        # MANAGE
        self.manageImage = Image.open('assets\\manage-icon.png')
        photo = ImageTk.PhotoImage(self.manageImage)
        self.manage = Label(self.sidebar, image=photo, bg='#ffffff')
        self.manage.image = photo
        self.manage.place(x=35, y=340)

        self.manage_text = Button(self.sidebar, text='Manage', bg='#ffffff', font=(
            '', 13, 'bold'), bd=0, cursor='hand2', activebackground='#ffffff')
        self.manage_text.place(x=80, y=345)

        # SETTINGS
        self.settingsImage = Image.open('assets\\settings-icon.png')
        photo = ImageTk.PhotoImage(self.settingsImage)
        self.settings = Label(self.sidebar, image=photo, bg='#ffffff')
        self.settings.image = photo
        self.settings.place(x=35, y=402)

        self.settings_text = Button(self.sidebar, text='Settings', bg='#ffffff', font=(
            '', 13, 'bold'), bd=0, cursor='hand2', activebackground='#ffffff')
        self.settings_text.place(x=80, y=402)

        # EXIT
        self.exitImage = Image.open('assets\\exit-icon.png')
        photo = ImageTk.PhotoImage(self.exitImage)
        self.exit = Label(self.sidebar, image=photo, bg='#ffffff')
        self.exit.image = photo
        self.exit.place(x=25, y=452)

        self.exit_text = Button(self.sidebar, text='Exit', bg='#ffffff', font=(
            '', 13, 'bold'), bd=0, cursor='hand2', activebackground='#ffffff')
        self.exit_text.place(x=85, y=462)

        #  USER NAME
        self.brandName = Label(
            self.sidebar, text='Bret Hart', bg='#ffffff', font=('', 15, 'bold'))
        self.brandName.place(x=80, y=200)

        # =================  BODY FRAME 1 ======================= #
        self.bodyFrame1 = Frame(self.window, bg='#ffffff')
        self.bodyFrame1.place(x=328, y=110, width=1040, height=350)

        # =================  BODY FRAME 2 ======================= #
        self.bodyFrame2 = Frame(self.window, bg='#009aa5')
        self.bodyFrame2.place(x=328, y=495, width=310, height=220)

        # =================  BODY FRAME 3 ======================= #
        self.bodyFrame3 = Frame(self.window, bg='#e21f26')
        self.bodyFrame3.place(x=680, y=495, width=310, height=220)

        # =================  BODY FRAME 4 ======================= #
        self.bodyFrame4 = Frame(self.window, bg='#ffcb1f')
        self.bodyFrame4.place(x=1030, y=495, width=310, height=220)


def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()


if __name__ == '__main__':
    win()
