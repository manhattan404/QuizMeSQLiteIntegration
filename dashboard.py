from tkinter import *
from PIL import ImageTk, Image

dashboard = Tk()
dashboard.geometry('900x500')
dashboard.configure(bg='#262626')
dashboard.resizable(0, 0)
dashboard.title('Quiz Me')


def toggle_win():
    f1 = Frame(dashboard, width=300, height=500, bg='#12c4c0')
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

    bttn(0, 80, 'A C E R', '#0f9d9a', '#12c4c0', None)
    bttn(0, 117, 'D E L L', '#0f9d9a', '#12c4c0', None)
    bttn(0, 154, 'A P P L E', '#0f9d9a', '#12c4c0', None)

    def dele():
        f1.destroy()

    global img2
    img2 = ImageTk.PhotoImage(Image.open('assets/close.png'))

    Button(f1, image=img2, command=dele, border=0,
           activebackground='#12c4c0', bg='#12c4c0').place(x=5, y=10)


img1 = ImageTk.PhotoImage(Image.open('assets/open.png'))
Button(dashboard, command=toggle_win, image=img1, border=0,
       bg='#262626', activebackground='#262626').place(x=5, y=10)

dashboard.mainloop()
