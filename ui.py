from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import ttk
import customtkinter
from customtkinter import *
from PIL import ImageTk, Image

grey_one = '#222222'
grey_two = '#333333'
light_black = '#111111'
black = '#000000'
grey_three = '#bbbbbb'

# -------------------------------------------------------------------------------------------------------------------------------------------------
# Create a frame that takes in question and answer and populate the SQL database

root = Tk()
root.title("SQL - Quiz Me")
root.geometry('1300x750+370+160')
root.configure(bg=grey_one)

# -------------------------------------------------------------------------------------------------------------------------------------------------
# ENTRY FRAME

question_var = tkinter.StringVar(value="Question")

question_label = customtkinter.CTkLabel(
    master=root,
    textvariable=question_var,
    width=120,
    height=25,
    text_color="white",
    corner_radius=8
)
question_label.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)


questionEntry = customtkinter.CTkEntry(
    master=root, 
    placeholder_text="Enter Your Question Here",
    width=120,
    height=25,
    border_width=2,
    corner_radius=10
    )
questionEntry.place(relx=0.25, rely=0.25, anchor=tkinter.CENTER)



# -------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()