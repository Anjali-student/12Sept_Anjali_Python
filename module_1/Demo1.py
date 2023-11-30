import tkinter
from tkinter import ttk,messagebox

screen=tkinter.Tk()
screen.geometry("500x600")
screen.config(bg='lightblue')
screen.title("TKApp")

tkinter.Label(text="Value 1:",bg='lightblue',fg='blue',font='Courier 15 bold').grid(row=0,column=0)
tkinter.Label(text="Value 2:",bg='lightblue',fg='blue',font='Courier 15 bold').grid(row=1,column=0)

txtfnm=tkinter.Entry()
txtfnm.grid(row=0,column=1,sticky='W')
txtlnm=tkinter.Entry()
txtlnm.grid(row=1,column=1,sticky='W')
a=int(txtfnm.get())
b=int(txtlnm.get())



def btnclickk():
    c=int(a-b)
    messagebox.showinfo("Answer",c)

def btnclickk3():

    c=int(a*b)
    messagebox.showinfo("Answer",c)


def btnclick():

    c=int(a+b)
    messagebox.showinfo("Answer",c)

def div():
    c=int(a/b)
    messagebox.showinfo("Answer",c)

tkinter.Button(text=" Add ",font='Courier 15 bold',command=btnclick).place(x=250,y=100)
tkinter.Button(text=" Sub ",font='Courier 15 bold',command=btnclickk).place(x=50,y=100)
tkinter.Button(text=" Mul ",font='Courier 15 bold',command=btnclickk3).place(x=150,y=100)
tkinter.Button(text=" Div ",font='Courier 15 bold',command=div).place(x=350,y=100)
tkinter.mainloop()
