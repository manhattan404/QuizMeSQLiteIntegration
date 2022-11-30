from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import ttk
import customtkinter
from customtkinter import *
from PIL import ImageTk, Image
import sqlite3
from Quizclass import *

conn = sqlite3.connect('questions.db')

c = conn.cursor()


def addButton():
    with conn:
        quest = questionEntry.get()
        ans = answerEntry.get()
        c.execute(
            "INSERT INTO questions VALUES (:question, :answer)", {'question': quest, 'answer': ans})
        print(quest + " and " + ans + " has been added to database")


def printData():
    
    c.execute("SELECT rowid, * FROM questions")
    records = c.fetchall()
    print(records)

grey_one = '#222222'
grey_two = '#333333'
light_black = '#111111'
black = '#000000'

root = Tk()
root.title("SQL - Quiz Me")
root.geometry('1300x750+370+160')
root.configure(bg=grey_one)


# -------------------------------------------------------------------------------------------------------------------------------------------------
### TREEVIEW ###



style = ttk.Style() # Add some style
style.theme_use('default') # Pick a theme
style.configure("Treeview", background="#D3D3D3", foreground="#black",rowheight=25,fieldbackground="D3D3D3") # Configure Treeview
style.map('Treeview', background=[('selected', "#347083")]) # change selected color
# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=100)
#Create a scroll bar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
# Create the actual treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()
# Configure the scrollbar 
tree_scroll.config(command=my_tree.yview)
# Define Columns
my_tree['columns'] = ("ID", "Question", "Answer")
# Formant our columns 
my_tree.column("#0", width=0, stretch=NO) # this is the hidden column that we want to hide by setting the width to 0
my_tree.column("ID", anchor=W, width=100)
my_tree.column("Question", anchor=CENTER, width=140)
my_tree.column("Answer", anchor=E, width=140)
# Create headings
my_tree.heading('#0', text="", anchor=W)
my_tree.heading('ID', text="ID", anchor=W)
my_tree.heading('Question', text="Question", anchor=CENTER)
my_tree.heading('Answer', text="Answer", anchor=E)

# -------------------------------------------------------------------------------------------------------------------------------------------------

question_var = tkinter.StringVar(value="Question")

question_label = customtkinter.CTkLabel(
    master=root,
    textvariable=question_var,
    width=200,
    height=50,
    text_color="white",
    corner_radius=8
)
question_label.place(x=100, y=100)


questionEntry = customtkinter.CTkEntry(
    master=root,
    placeholder_text="Enter Your Question Here",
    width=200,
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
    width=200,
    height=50,
    text_color="white",
    corner_radius=8
)
answer_label.place(x=100, y=250)


answerEntry = customtkinter.CTkEntry(
    master=root,
    placeholder_text="Enter Your Answer Here",
    width=200,
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
    command=addButton
)
add_button.place(x=100, y=400)


# -------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()
