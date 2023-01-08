from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3

dashboard = Tk()
dashboard.geometry('1300x750+370+160')
dashboard.configure(bg='#262626')
dashboard.resizable(0, 0)
dashboard.title('Quiz Me')


def toggle_win():
    f1 = Frame(dashboard, width=300, height=750, bg='#12c4c0')
    f1.place(x=0, y=0)

    def bttn(x, y, text, bcolor, fcolor, cmd):

        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'

        def on_leave(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text, width=42, height=2, fg='#262626', border=0,
                           bg=fcolor, activeforeground='#262626', activebackground=bcolor, command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leave)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'T A K E Q U I Z', '#0f9d9a', '#12c4c0', None)
    bttn(0, 117, 'S H O W Q U I Z', '#0f9d9a', '#12c4c0', displayonTreeview)
    bttn(0, 154, 'S C O R E S', '#0f9d9a', '#12c4c0', None)

    def dele():
        f1.destroy()

    global img2
    img2 = ImageTk.PhotoImage(Image.open('assets/close.png'))

    Button(f1, image=img2, command=dele, border=0,
           activebackground='#12c4c0', bg='#12c4c0').place(x=5, y=10)


img1 = ImageTk.PhotoImage(Image.open('assets/open.png'))
Button(dashboard, command=toggle_win, image=img1, border=0,
       bg='#262626', activebackground='#262626').place(x=5, y=10)


# -------------------------------------------------------------------------------------------------------------------------------------------------
### TREEVIEW ###


def displayonTreeview():

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="#black",
                    rowheight=25, fieldbackground="D3D3D3")
    style.map('Treeview', background=[('selected', "#347083")])

    tree_frame = Frame(dashboard)
    tree_frame.pack(pady=100)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Create the actual treeview
    my_tree = ttk.Treeview(
        tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()
    # Configure the scrollbar
    tree_scroll.config(command=my_tree.yview)

    # Define Columns
    my_tree['columns'] = ("ID", "Question", "Answer")
    # Formant our columns
    # this is the hidden column that we want to hide by setting the width to 0
    my_tree.column("#0", width=0, stretch=NO)
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

    conn = sqlite3.connect('questions.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM questions")
    records = c.fetchall()

    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[0], record[1], record[2]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(
                record[0], record[1], record[2]), tags=('oddrow',))

        count += 1

    conn.commit()
    conn.close()


# -------------------------------------------------------------------------------------------------------------------------------------------------


dashboard.mainloop()
