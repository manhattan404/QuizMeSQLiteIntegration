from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import customtkinter
from customtkinter import *
from PIL import ImageTk, Image
import sqlite3

background = 'white'
box_color = '#F0EBE3'
grey_one = '#222222'
grey_two = '#333333'
light_black = '#111111'
black = '#000000'

mainwindow = Tk()
mainwindow.title("SQL - Quiz Me")
mainwindow.geometry('1300x750+370+160')
mainwindow.configure(bg=grey_two)
mainwindow.resizable(False, False)


sideframe = tk.Frame(mainwindow, bg=grey_one)
sideframe.pack(side=tk.LEFT)
sideframe.pack_propagate(False)
sideframe.configure(width=300, height=750)


main_frame = tk.Frame(
    mainwindow, bg=background)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=1000, height=750)

# topframe = customtkinter.CTkFrame(
#     master=mainwindow, width=1068, height=250, corner_radius=30, fg_color=box_color)
# topframe.place(x=400, y=20)

# midframe = customtkinter.CTkFrame(
#     master=mainwindow, width=1068, height=517, corner_radius=30, fg_color=box_color)
# midframe.place(x=400, y=305)


mainwindow.mainloop()
