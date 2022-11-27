from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import ttk
import customtkinter
from customtkinter import *
from PIL import ImageTk, Image
import main

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

question_var = tkinter.StringVar(value="Question")

question_label = customtkinter.CTkLabel(
    master=root,
    textvariable=question_var,
    width=400,
    height=50,
    text_color="white",
    corner_radius=8
)
question_label.place(x=100, y=100)


questionEntry = customtkinter.CTkEntry(
    master=root, 
    placeholder_text="Enter Your Question Here",
    width=400,
    height=50,
    border_width=2,
    corner_radius=10
    )
questionEntry.place(x=100, y=150)
# -------------------------------------------------------------------------------------------------------------------------------------------------

answer_var = tkinter.StringVar(value="Answer")

answer_label = customtkinter.CTkLabel(
    master=root,
    textvariable=answer_var,
    width=400,
    height=50,
    text_color="white",
    corner_radius=8
)
answer_label.place(x=100, y=250)


answerEntry = customtkinter.CTkEntry(
    master=root, 
    placeholder_text="Enter Your Answer Here",
    width=400,
    height=50,
    border_width=2,
    corner_radius=10
    )
answerEntry.place(x=100, y=300)


# -------------------------------------------------------------------------------------------------------------------------------------------------
# ADD BUTTON

add_button = customtkinter.CTkButton(
    master=root,
    width=120,
    height=32,
    border_width=0,
    corner_radius=8,
    text="Add",    
    command=main.addButton
)
add_button.place(x=100, y=400)



# -------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()