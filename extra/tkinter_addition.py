import tkinter
from tkinter import ttk, messagebox


screen = tkinter.Tk()
screen.geometry("500x600")
screen.config(bg='lightblue')
screen.title("TKApp")

tkinter.Label(text="Value 1:", bg='lightblue', fg='blue', font='Courier 15 bold').grid(row=0, column=0)
tkinter.Label(text="Value 2:", bg='lightblue', fg='blue', font='Courier 15 bold').grid(row=1, column=0)

txtfnm = tkinter.Entry()
txtfnm.grid(row=0, column=1, sticky='W')
txtlnm = tkinter.Entry()
txtlnm.grid(row=1, column=1, sticky='W')

a =txtfnm.get()
b =txtlnm.get()


def sub_btn():
    a1=int(txtfnm.get())
    a2=int(txtlnm.get())
    c=a1-a2
    messagebox.showinfo("Answer",f"The subtraction of {a1} and {a2} is:{c}")


tkinter.Button(text=" Sub ", font='Courier 15 bold', command=sub_btn).place(x=50, y=100)


def mult_btn():
    a1 = int(txtfnm.get())
    a2 = int(txtlnm.get())
    c = int(a1 * a2)
    messagebox.showinfo("Answer",f"The Multiplication of {a1} and {a2} is:{c}")


tkinter.Button(text=" Mul ", font='Courier 15 bold', command=mult_btn).place(x=150, y=100)


def add_btn():
    a1 = int(txtfnm.get())
    a2 = int(txtlnm.get())
    c = int(a1 + a2)
    messagebox.showinfo("Answer:",f"The addition of {a1} and {a2} is:{c}")


tkinter.Button(text=" Add ", font='Courier 15 bold', command=add_btn).place(x=250, y=100)


def div_btn():
    a1 = int(txtfnm.get())
    a2 = int(txtlnm.get())
    try:
        c = int(a1 / a2)
    except Exception as e:
        messagebox.showinfo(e)
    else:
        messagebox.showinfo("Answer",f"The division of {a1} and {a2} is:{c}")


tkinter.Button(text=" Div ", font='Courier 15 bold', command=div_btn).place(x=350, y=100)
tkinter.mainloop()
