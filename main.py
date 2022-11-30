from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import ttk
import customtkinter
from customtkinter import *
from PIL import ImageTk, Image
import sqlite3

grey_one = '#222222'
grey_two = '#333333'
light_black = '#111111'
black = '#000000'

root = Tk()
root.title("SQL - Quiz Me")
root.geometry('1300x750+370+160')
root.configure(bg=grey_one)

conn = sqlite3.connect('questions.db')

c = conn.cursor()



def addButton():
    
    
    with conn:
        quest = questionEntry.get()
        ans = answerEntry.get()
        c.execute(
            "INSERT INTO questions VALUES (:question, :answer)", {'question': quest, 'answer': ans})

        questionEntry.delete(0, END)
        answerEntry.delete(0, END)

        my_tree.delete(*my_tree.get_children())



def printData():
    
    c.execute("SELECT rowid, * FROM questions")
    records = c.fetchall()
    print(records)


def displayonTreeview():
    conn = sqlite3.connect('questions.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM questions")
    records = c.fetchall()

    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1], record[2]), tags=('evenrow',))
        else: 
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1], record[2]), tags=('oddrow',))

        count += 1

    conn.commit()
    conn.close()


def delete_one():
    curItem = my_tree.focus()
    valueList=my_tree.item(curItem, 'values')
    global selectedItem2
    selectedItem2=valueList[0]
    questID = my_tree.selection()[0]
    my_tree.delete(questID)
    conn87 = sqlite3.connect('questions.db')
    c87 = conn87.cursor()

    delete_query = str(f"""DELETE FROM questions WHERE oid=""") + selectedItem2
    c87.execute(str(delete_query))

    conn87.commit()
    conn87.close()



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
my_tree.column("ID", anchor=CENTER, width=70)
my_tree.column("Question", anchor=W, width=400)
my_tree.column("Answer", anchor=CENTER, width=180)
# Create headings
my_tree.heading('#0', text="", anchor=W)
my_tree.heading('ID', text="Question ID ", anchor=CENTER)
my_tree.heading('Question', text="Question", anchor=CENTER)
my_tree.heading('Answer', text="Answer", anchor=CENTER)
# Create fake data
# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")


# -------------------------------------------------------------------------------------------------------------------------------------------------
### BUTTONS AND ENTRIES ###



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


delete_button = customtkinter.CTkButton(
    master=root,
    width=120,
    height=32,
    border_width=0,
    corner_radius=8,
    text="Delete",
    command=delete_one
)
delete_button.place(x=100, y=500)

# -------------------------------------------------------------------------------------------------------------------------------------------------


displayonTreeview()

root.mainloop()
