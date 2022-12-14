from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import ttk
import customtkinter
from customtkinter import *
from PIL import ImageTk, Image
import sqlite3

background = 'white'
box_color = '#F0EBE3'

mainwindow = Tk()
mainwindow.title("SQL - Quiz Me")
mainwindow.geometry('1500x850+590+320')
mainwindow.configure(bg=background)
mainwindow.resizable(False, False)


sideframe = customtkinter.CTkFrame(master=mainwindow, width=335, height=800, corner_radius=30, fg_color=box_color)
sideframe.place(x=30, y=20)

topframe = customtkinter.CTkFrame(master=mainwindow, width=1068, height=250, corner_radius=30, fg_color=box_color)
topframe.place(x=400, y=20)

midframe = customtkinter.CTkFrame(master=mainwindow, width=1068, height=517, corner_radius=30, fg_color=box_color)
midframe.place(x=400, y=305)





mainwindow.mainloop()