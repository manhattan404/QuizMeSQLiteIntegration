import tkinter as tk
from tkinter import *
import sqlite3
import customtkinter
from customtkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

grey_one = '#222222'

root = tk.Tk()
root.title("Quiz Me by Szhes")


x = int(root.winfo_screenwidth() // 2.5)
y = int(root.winfo_screenheight() * 0.15)
root.geometry('350x600' + '+' + str(x) + '+' + str(y))

welcome_bg = ImageTk.PhotoImage(Image.open('assets/welcome.png'))
welcome_bg_label = Label(root, image=welcome_bg)
welcome_bg_label.pack()


root.configure(bg=grey_one)
root.resizable(False, False)


root.mainloop()
