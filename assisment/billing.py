import tkinter
from tkinter import ttk,messagebox
import mysql.connector

screen=tkinter.Tk()
screen.geometry("500x600")
screen.config(bg='lightblue')
screen.title("TKApp")

"""tkinter.Label(text="Firstname:").pack()
tkinter.Label(text="Lastname:").pack()"""

"""tkinter.Label(text="Firstname:").place(x=0,y=0)
tkinter.Label(text="Lastname:").place(x=0,y=20)"""

tkinter.Label(text="Firstname:",bg='lightblue',fg='blue',font='Courier 15 bold').grid(row=0,column=0)
tkinter.Label(text="Lastname:",bg='lightblue',fg='blue',font='Courier 15 bold').grid(row=1,column=0)

txtfnm=tkinter.Entry()
txtfnm.grid(row=0,column=1,sticky='W')
txtlnm=tkinter.Entry()
txtlnm.grid(row=1,column=1,sticky='W')


tkinter.Radiobutton(value=0,text="Male",bg='lightblue',fg='blue',font='Courier 15 bold').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1,text="Female",bg='lightblue',fg='blue',font='Courier 15 bold').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text="Gujarati",bg='lightblue',fg='blue',font='Courier 15 bold').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text="Hindi",bg='lightblue',fg='blue',font='Courier 15 bold').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text="English",bg='lightblue',fg='blue',font='Courier 15 bold').grid(row=5,column=0,sticky='W')


city=['Rajkot','Ahmedabad','Surat','Baroda','Gandhinagar']
ttk.Combobox(values=city).grid(row=6,column=0)

def btnclick():
    #print("Button clicked!")
    #messagebox.showerror("Error","Something went wrong...Try again!")
    #messagebox.showinfo("Success","Your data has been submitted!")
    #messagebox.showwarning("Warning","Your disk is full!")

    #messagebox.askokcancel("Download","Do you want to continue?")
    #messagebox.askquestion("Download","Do you want to continue?")
    #messagebox.askretrycancel("Download","Do you want to continue?")
    #messagebox.askyesno("Download","Do you want to continue?")
    #messagebox.askyesnocancel("Download","Do you want to continue?")

    print("Firstname:",txtfnm.get())
    print("Lastname:",txtlnm.get())
    messagebox.showinfo("Studetdata",f"Firstname:{txtfnm.get()} and Lastname:{txtlnm.get()}")

tkinter.Button(text="Submit",font='Courier 15 bold',command=btnclick).place(x=220,y=250)
tkinter.mainloop()