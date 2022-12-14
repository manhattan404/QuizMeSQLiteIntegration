from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3

whitebg = '#F9F9F9'
bluebg = '#39B5E0'
greybg = '#222222'

dashboard = Tk()
dashboard.geometry('1300x750+370+160')
dashboard.configure(bg=whitebg)
dashboard.resizable(0, 0)
dashboard.title('Quiz Me')


def toggle_win():
    f1 = Frame(dashboard, width=300, height=750, bg='#262626')
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
    bttn(0, 117, 'S H O W Q U I Z', '#0f9d9a', '#12c4c0', None)
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

    my_tree = ttk.Treeview(
        tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ("ID", "Question", "Answer")

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID", anchor=CENTER, width=70)
    my_tree.column("Question", anchor=W, width=400)
    my_tree.column("Answer", anchor=CENTER, width=180)

    my_tree.heading('#0', text="", anchor=W)
    my_tree.heading('ID', text="Question ID ", anchor=CENTER)
    my_tree.heading('Question', text="Question", anchor=CENTER)
    my_tree.heading('Answer', text="Answer", anchor=CENTER)

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
### TOPICS FRAME ###


topics_frame = Frame(dashboard, width=955, height=700, bg=whitebg)
topics_frame.place(x=325, y=25)
folders_frame = Frame(topics_frame, width=955, height=550, bg=greybg)
folders_frame.place(x=0, y=150)
topics_label = Label(topics_frame, text='TOPICS',
                     font=('Expo M', 80), fg=greybg)
topics_label.place(x=20, y=20)

# topicsFrame = customtkinter.CTkFrame(
#     master=dashboard, width=955, height=700, corner_radius=15, bg_color=whitebg)
# topicsFrame.place(x=325, y=25)
# foldersFrame = customtkinter.CTkFrame(
#     master=topicsFrame, width=955, height=550, corner_radius=15, bg_color='#222222')
# foldersFrame.place(x=0, y=150)
# topics_label = customtkinter.CTkLabel(
#     master=topicsFrame, text='TOPICS', width=120, height=120, font=('Expo M', 100))
# topics_label.place(x=25, y=20)
# -------------------------------------------------------------------------------------------------------------------------------------------------

toggle_win()
dashboard.mainloop()
