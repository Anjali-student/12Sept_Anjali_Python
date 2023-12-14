from tkinter import *
from tkinter import messagebox
import random, os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)
mycursor = mydb.cursor(buffered=True)

billnumber = random.randint(500, 1000)


def exit_screen():
    res = messagebox.askquestion('Exit Application', 'Do you really want to exit')
    if res == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'Returning to main application')


def clear_file():
    bath_entry.delete(0, END)
    face_entry.delete(0, END)
    facewash_entry.delete(0, END)
    hairspray_entry.delete(0, END)
    lotion_entry.delete(0, END)

    rice_entry.delete(0, END)
    oil_entry.delete(0, END)
    dall_entry.delete(0, END)
    wheat_entry.delete(0, END)
    sugar_entry.delete(0, END)

    maza_entry.delete(0, END)
    coke_entry.delete(0, END)
    frooti_entery.delete(0, END)
    nimkos_Entry.delete(0, END)
    biscuit_entry.delete(0, END)

    bath_entry.insert(0, 0)
    face_entry.insert(0, 0)
    facewash_entry.insert(0, 0)
    hairspray_entry.insert(0, 0)
    lotion_entry.insert(0, 0)

    rice_entry.insert(0, 0)
    oil_entry.insert(0, 0)
    dall_entry.insert(0, 0)
    wheat_entry.insert(0, 0)
    sugar_entry.insert(0, 0)

    maza_entry.insert(0, 0)
    coke_entry.insert(0, 0)
    frooti_entery.insert(0, 0)
    nimkos_Entry.insert(0, 0)
    biscuit_entry.insert(0, 0)

    total_cosmetics.delete(0, END)
    Cos_tax_entry.delete(0, END)
    tital_gro.delete(0, END)
    grocery_tax_entry.delete(0, END)
    other_total_entry.delete(0, END)
    other_tax.delete(0, END)

    cname_Entry.delete(0, END)
    cphone.delete(0, END)
    bill_entry_search.delete(0, END)
    textrea.delete(1.0, END)


def serach_bill():
    for i in os.listdir('bills/'):
        if i.split(".")[0] == bill_entry_search.get():
            f1 = open(f'bills/{i}', 'r')
            textrea.delete(1.0, END)
            for data in f1:
                textrea.insert(END, data)
            f1.close()
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you Want to Save and store data of the Bill?')
    if result:
        bill_content = textrea.get(1.0, END)
        f = open(f'bills/{billnumber}.txt', 'w')
        f.write((bill_content))
        f.close()
        messagebox.showinfo('Success', f'Bill Number {billnumber} is saved Successfully')
        billnumber = random.randint(500, 1000)
        sql = (f'INSERT INTO billing_records (bill_no,phoneNo,Cname,BathSoap,FaceCream,FaceWash,HairSpray,BodyLotion,'
               f'Rice,FoodOil,Daal,Wheat,Suger,Maza,Coke,Frooti,Nimkos,Biscuits,Total_Cos,Total_Groc,Total_oth,'
               f'Cos_tax,Gro_tax,Oth_tax,Total_bill) values("{billnumber}","{cphone.get()}","{cname_Entry.get()}",'
               f'"{bath_entry.get()}","{face_entry.get()}","{facewash_entry.get()}","{hairspray_entry.get()}",'
               f'"{lotion_entry.get()}","{rice_entry.get()}","{oil_entry.get()}","{dall_entry.get()}",'
               f'"{wheat_entry.get()}","{sugar_entry.get()}","{maza_entry.get()}",{coke_entry.get()},'
               f'"{nimkos_Entry.get()}","{frooti_entery.get()}","{biscuit_entry.get()}","{total_cosmetics.get()}",'
               f'"{tital_gro.get()}","{other_total_entry.get()}","{Cos_tax_entry.get()}","{grocery_tax_entry.get()}",'
               f'"{other_tax.get()}","{total_bill}")')
        try:
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            print(e)


def billarea():
    if cname_Entry.get() == '' or cphone.get() == '':
        messagebox.showerror("Error", "Customer Details are Required!")
    elif total_cosmetics.get() == '' and tital_gro.get() == '' and other_total_entry.get() == '':
        messagebox.showerror("Error", "Please Selects Any Products.")
    elif total_cosmetics.get() == '0 Rs' and tital_gro.get() == '0 Rs' and other_total_entry.get() == '0 Rs':
        messagebox.showerror("Error..", "Please Selects Any Products.")
    else:
        textrea.delete(1.0, END)
        textrea.insert(END, '\t**Welcome Customer**\n')
        textrea.insert(END, f'\nBill Number: {billnumber}')
        textrea.insert(END, f'\nCustomer Name: {cname_Entry.get()}')
        textrea.insert(END, f'\nCustomer Phone No.: {cphone.get()}')
        textrea.insert(END, '\n=====================================')
        textrea.insert(END, '\nProduct\t\tQTY\t\tPrice')
        textrea.insert(END, '\n=====================================')
        # cosmeticsq
        if bath_entry.get() != '0':
            textrea.insert(END, f'\nBath Soap\t\t{bath_entry.get()}\t\t{bath_soap}')
        if face_entry.get() != '0':
            textrea.insert(END, f'\nFace Cream\t\t{face_entry.get()}\t\t{face_creame}')
        if facewash_entry.get() != '0':
            textrea.insert(END, f'\nface wash\t\t{facewash_entry.get()}\t\t{face_wash}')
        if hairspray_entry.get() != '0':
            textrea.insert(END, f'\nHair Spray\t\t{hairspray_entry.get()}\t\t{hair_spray}')
        if lotion_entry.get() != '0':
            textrea.insert(END, f'\nBody Lotion\t\t{lotion_entry.get()}\t\t{body_lotion}')
        # grocery
        if rice_entry.get() != '0':
            textrea.insert(END, f'\nRice\t\t{rice_entry.get()}\t\t{rice}')
        if oil_entry.get() != '0':
            textrea.insert(END, f'\nFood Oil\t\t{oil_entry.get()}\t\t{food_oli}')
        if dall_entry.get() != '0':
            textrea.insert(END, f'\nDaal\t\t{dall_entry.get()}\t\t{daal2}')
        if wheat_entry.get() != '0':
            textrea.insert(END, f'\nWheat\t\t{wheat_entry.get()}\t\t{wheatt}')
        if sugar_entry.get() != '0':
            textrea.insert(END, f'\nSuger\t\t{sugar_entry.get()}\t\t{sugerr}')
        # others
        if maza_entry.get() != '0':
            textrea.insert(END, f'\nMaza\t\t{maza_entry.get()}\t\t{maza1}')
        if coke_entry.get() != '0':
            textrea.insert(END, f'\nCoke\t\t{coke_entry.get()}\t\t{coke1}')
        if frooti_entery.get() != '0':
            textrea.insert(END, f'\nFrooti\t\t{frooti_entery.get()}\t\t{frooti1}')
        if nimkos_Entry.get() != '0':
            textrea.insert(END, f'\nNumkos\t\t{nimkos_Entry.get()}\t\t{nimkos1}')
        if biscuit_entry.get() != '0':
            textrea.insert(END, f'\nBiscuits\t\t{biscuit_entry.get()}\t\t{biscuit1}')
        textrea.insert(END, '\n-------------------------------------')
        if Cos_tax_entry.get() != '0.0RS':
            textrea.insert(END, f'\nCosmetics Tax\t\t\t{Cos_tax_entry.get()}')
        if grocery_tax_entry.get() != '0.0RS':
            textrea.insert(END, f'\nGrocery Tax\t\t\t{grocery_tax_entry.get()}')
        if other_total_entry.get() != '0.0RS':
            textrea.insert(END, f'\nOther Tax\t\t\t{other_total_entry.get()}')
        textrea.insert(END, f'\n\nTotal Bill\t\t\t{total_bill}')
        textrea.insert(END, '\n-------------------------------------')
        save_bill()


def total():
    global bath_soap, face_creame, face_wash, hair_spray, body_lotion, rice, food_oli, daal2, wheatt, sugerr
    global maza1, coke1, frooti1, nimkos1, biscuit1, total_bill
    # Cosmetics Total
    bath_soap = int(bath_entry.get()) * 20
    face_creame = int(face_entry.get()) * 50
    face_wash = int(facewash_entry.get()) * 100
    hair_spray = int(hairspray_entry.get()) * 150
    body_lotion = int(lotion_entry.get()) * 70
    total_cost = bath_soap + face_creame + face_wash + hair_spray + body_lotion
    total_cosmetics.delete(0, END)
    total_cosmetics.insert(0, f'{total_cost} Rs')
    cosmetics_tax = total_cost * 0.12
    Cos_tax_entry.delete(0, END)
    Cos_tax_entry.insert(0, str(cosmetics_tax) + 'Rs')

    # Grocery Tatal
    rice = int(rice_entry.get()) * 80
    food_oli = int(oil_entry.get()) * 200
    daal2 = int(dall_entry.get()) * 150
    wheatt = int(wheat_entry.get()) * 80
    sugerr = int(sugar_entry.get()) * 170
    total_groceries_price = rice + food_oli + daal2 + wheatt + sugerr
    tital_gro.delete(0, END)
    tital_gro.insert(0, f'{total_groceries_price} Rs')
    grocery_tax1 = total_groceries_price * 0.05
    grocery_tax_entry.delete(0, END)
    grocery_tax_entry.insert(0, str(grocery_tax1) + 'Rs')

    # others total
    maza1 = int(maza_entry.get()) * 20
    coke1 = int(coke_entry.get()) * 10
    frooti1 = int(frooti_entery.get()) * 10
    nimkos1 = int(nimkos_Entry.get()) * 10
    biscuit1 = int(biscuit_entry.get()) * 10
    other_totals = maza1 + coke1 + frooti1 + nimkos1 + biscuit1
    other_total_entry.delete(0, END)
    other_total_entry.insert(0, f'{other_totals} Rs')
    other_tax1 = other_totals * 0.12
    other_tax.delete(0, END)
    other_tax.insert(0, str(other_tax1) + 'Rs')

    # total
    total_bill = total_cost + total_groceries_price + other_totals + cosmetics_tax + grocery_tax1 + other_tax1


root = Tk()
root.title("Billing Software")
root.geometry('1024x1024')
root.config()
lb = Label(root, text='Billing Software', bg='dark blue', fg='white', font='Courier 25 bold', bd=12, relief=GROOVE)
lb.pack(fill=X, pady=2, padx=2)

cdetail_frame = LabelFrame(root, text="Customer Details", font='Courier 10 bold', fg='Yellow', bg='dark blue',
                           relief=GROOVE, bd=3)
cdetail_frame.pack(fill=X)
cname_label = Label(cdetail_frame, text="Customer Name ", font='Courier 10 bold', bg='dark blue', fg='white')
cname_label.grid(row=0, column=0, padx=4)
cname_Entry = Entry(cdetail_frame, font='Courier 10 bold', bd=3)
cname_Entry.grid(row=0, column=1, padx=10)

cphone_label = Label(cdetail_frame, text="Phone No.", font='Courier 10 bold', bg='dark blue', fg='white')
cphone_label.grid(row=0, column=2, padx=4)
cphone = Entry(cdetail_frame, font='Courier 10 bold', bd=3)
cphone.grid(row=0, column=3, padx=10)

billno_label = Label(cdetail_frame, text="Bill No.", font='Courier 10 bold', bg='dark blue', fg='white')
billno_label.grid(row=0, column=4, padx=4)
bill_entry_search = Entry(cdetail_frame, font='Courier 10 bold', bd=3)
bill_entry_search.grid(row=0, column=5, padx=10)

enter_btn = Button(cdetail_frame, text="Enter", font='Courier 10 bold', bg='dark blue', fg='white', bd=7,
                   command=serach_bill)
enter_btn.grid(row=0, column=6, padx=20, pady=8)

product_frame = Frame(root, bd=3, relief=GROOVE)
product_frame.pack(fill=X)
cosmetic_frame = LabelFrame(product_frame, text="Cosmetics", font='Courier 10 bold', fg='Yellow', bg='dark blue',
                            relief=GROOVE, bd=3)
cosmetic_frame.grid(row=0, column=0)

label_bath = Label(cosmetic_frame, text="Bath Soap", font='Courier 10 bold', bg='dark blue', fg='white')
label_bath.grid(row=0, column=0, pady=15, padx=5, sticky='W')
bath_entry = Entry(cosmetic_frame, font='Courier 10 bold', width=15, bd=3)
bath_entry.grid(row=0, column=1, pady=15, padx=5)
bath_entry.insert(0, 0)

lable_cream = Label(cosmetic_frame, text="Face Cream", font='Courier 10 bold', bg='dark blue', fg='white')
lable_cream.grid(row=1, column=0, pady=15, padx=5, sticky='W')
face_entry = Entry(cosmetic_frame, font='Courier 10 bold', width=15, bd=3)
face_entry.grid(row=1, column=1, pady=15, padx=5)
face_entry.insert(0, 0)

vabel_face_wash = Label(cosmetic_frame, text="Face Wash", font='Courier 10 bold', bg='dark blue', fg='white')
vabel_face_wash.grid(row=2, column=0, pady=15, padx=5, sticky='W')
facewash_entry = Entry(cosmetic_frame, font='Courier 10 bold', width=15, bd=3)
facewash_entry.grid(row=2, column=1, pady=15, padx=5)
facewash_entry.insert(0, 0)

label_hair = Label(cosmetic_frame, text="Hair Spray", font='Courier 10 bold', bg='dark blue', fg='white')
label_hair.grid(row=3, column=0, pady=15, padx=5, sticky='W')
hairspray_entry = Entry(cosmetic_frame, font='Courier 10 bold', width=15, bd=3)
hairspray_entry.grid(row=3, column=1, pady=15, padx=5)
hairspray_entry.insert(0, 0)

label_body = Label(cosmetic_frame, text="Body Lotion", font='Courier 10 bold', bg='dark blue', fg='white')
label_body.grid(row=4, column=0, pady=15, padx=5, sticky='W')
lotion_entry = Entry(cosmetic_frame, font='Courier 10 bold', width=15, bd=3)
lotion_entry.grid(row=4, column=1, pady=15, padx=5)
lotion_entry.insert(0, 0)

grocery_frame = LabelFrame(product_frame, text="Grocery", font='Courier 10 bold', fg='Yellow', bg='dark blue',
                           relief=GROOVE, bd=3)
grocery_frame.grid(row=0, column=1)

label_rice = Label(grocery_frame, text="Rice", font='Courier 10 bold', bg='dark blue', fg='white')
label_rice.grid(row=0, column=0, pady=15, padx=5, sticky='W')
rice_entry = Entry(grocery_frame, font='Courier 10 bold', width=15, bd=3)
rice_entry.grid(row=0, column=1, pady=15, padx=5)
rice_entry.insert(0, 0)

lable_oil = Label(grocery_frame, text="Food Oil", font='Courier 10 bold', bg='dark blue', fg='white')
lable_oil.grid(row=1, column=0, pady=15, padx=5, sticky='W')
oil_entry = Entry(grocery_frame, font='Courier 10 bold', width=15, bd=3)
oil_entry.grid(row=1, column=1, pady=15, padx=5)
oil_entry.insert(0, 0)

dall_label = Label(grocery_frame, text="Daal", font='Courier 10 bold', bg='dark blue', fg='white')
dall_label.grid(row=2, column=0, pady=15, padx=5, sticky='W')
dall_entry = Entry(grocery_frame, font='Courier 10 bold', width=15, bd=3)
dall_entry.grid(row=2, column=1, pady=15, padx=5)
dall_entry.insert(0, 0)

wheat_label = Label(grocery_frame, text="Wheat", font='Courier 10 bold', bg='dark blue', fg='white')
wheat_label.grid(row=3, column=0, pady=15, padx=5, sticky='W')
wheat_entry = Entry(grocery_frame, font='Courier 10 bold', width=15, bd=3)
wheat_entry.grid(row=3, column=1, pady=15, padx=5)
wheat_entry.insert(0, 0)

sugar_label = Label(grocery_frame, text="Sugar", font='Courier 10 bold', bg='dark blue', fg='white')
sugar_label.grid(row=4, column=0, pady=15, padx=5, sticky='W')
sugar_entry = Entry(grocery_frame, font='Courier 10 bold', width=15, bd=3)
sugar_entry.grid(row=4, column=1, pady=15, padx=5)
sugar_entry.insert(0, 0)

other_frame = LabelFrame(product_frame, text="others", font='Courier 10 bold', fg='Yellow', bg='dark blue',
                         relief=GROOVE, bd=3)
other_frame.grid(row=0, column=2)

maza_label = Label(other_frame, text="Maza", font='Courier 10 bold', bg='dark blue', fg='white')
maza_label.grid(row=0, column=0, pady=15, padx=5, sticky='W')
maza_entry = Entry(other_frame, font='Courier 10 bold', width=15, bd=3)
maza_entry.grid(row=0, column=1, pady=15, padx=5)
maza_entry.insert(0, 0)

coke_label = Label(other_frame, text="Coke", font='Courier 10 bold', bg='dark blue', fg='white')
coke_label.grid(row=1, column=0, pady=15, padx=5, sticky='W')
coke_entry = Entry(other_frame, font='Courier 10 bold', width=15, bd=3)
coke_entry.grid(row=1, column=1, pady=15, padx=5)
coke_entry.insert(0, 0)

frooti_label = Label(other_frame, text="Frooti", font='Courier 10 bold', bg='dark blue', fg='white')
frooti_label.grid(row=2, column=0, pady=15, padx=5, sticky='W')
frooti_entery = Entry(other_frame, font='Courier 10 bold', width=15, bd=3)
frooti_entery.grid(row=2, column=1, pady=15, padx=5)
frooti_entery.insert(0, 0)

nimkos_label = Label(other_frame, text="Nimkos", font='Courier 10 bold', bg='dark blue', fg='white')
nimkos_label.grid(row=3, column=0, pady=15, padx=5, sticky='W')
nimkos_Entry = Entry(other_frame, font='Courier 10 bold', width=15, bd=3)
nimkos_Entry.grid(row=3, column=1, pady=15, padx=5)
nimkos_Entry.insert(0, 0)

biscuit_label = Label(other_frame, text="Biscuits", font='Courier 10 bold', bg='dark blue', fg='white')
biscuit_label.grid(row=4, column=0, pady=15, padx=5, sticky='W')
biscuit_entry = Entry(other_frame, font='Courier 10 bold', width=15, bd=3)
biscuit_entry.grid(row=4, column=1, pady=15, padx=5)
biscuit_entry.insert(0, 0)

bill_Frame = Frame(product_frame, bd=3, relief=GROOVE)
bill_Frame.grid(row=0, column=3, )

bil_area_label = Label(bill_Frame, text="Bill Area", font='Courier 12 bold', bd=3, relief=GROOVE)
bil_area_label.pack(fill=X)
scroll_bar = Scrollbar(bill_Frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=Y)
textrea = Text(bill_Frame, height="16", width="38", yscrollcommand=scroll_bar.set)
textrea.pack()
scroll_bar.config(command=textrea.yview)

Bill_name = LabelFrame(root, text="Bill Menu", font='Courier 10 bold', fg='Yellow', bg='dark blue', relief=GROOVE, bd=3)
Bill_name.pack(fill=X)

total_cosmetics_label = Label(Bill_name, text="Total Cosmetics", font='Courier 10 bold', bg='dark blue', fg='white')
total_cosmetics_label.grid(row=0, column=0, padx=4)
total_cosmetics = Entry(Bill_name, font='Courier 10 bold', width=15, bd=3)
total_cosmetics.grid(row=0, column=1, pady=10, padx=10)

tatal_grocery = Label(Bill_name, text="Total Grocery ", font='Courier 10 bold', bg='dark blue', fg='white')
tatal_grocery.grid(row=1, column=0, padx=4)
tital_gro = Entry(Bill_name, font='Courier 10 bold', width=15, bd=3)
tital_gro.grid(row=1, column=1, pady=10, padx=10)

other_total = Label(Bill_name, text="Others Total ", font='Courier 10 bold', bg='dark blue', fg='white')
other_total.grid(row=2, column=0, padx=4)
other_total_entry = Entry(Bill_name, font='Courier 10 bold', width=15, bd=3)
other_total_entry.grid(row=2, column=1, pady=10, padx=10)

# Tax

Cosmetics_tax = Label(Bill_name, text="Cosmetics Tax", font='Courier 10 bold', bg='dark blue', fg='white')
Cosmetics_tax.grid(row=0, column=3, pady=5, padx=5, sticky='W')
Cos_tax_entry = Entry(Bill_name, font='Courier 10 bold', width=15, bd=3)
Cos_tax_entry.grid(row=0, column=4, pady=10, padx=10)

grocery_tax = Label(Bill_name, text="Grocery Tax", font='Courier 10 bold', bg='dark blue', fg='white')
grocery_tax.grid(row=1, column=3, pady=10, padx=5, sticky='W')
grocery_tax_entry = Entry(Bill_name, font='Courier 10 bold', width=15, bd=3)
grocery_tax_entry.grid(row=1, column=4, pady=10, padx=10)

other_label = Label(Bill_name, text="Others Tax", font='Courier 10 bold', bg='dark blue', fg='white')
other_label.grid(row=2, column=3, pady=10, padx=5, sticky='W')
other_tax = Entry(Bill_name, font='Courier 10 bold', width=15, bd=3)
other_tax.grid(row=2, column=4, padx=10)

total_btn = Button(Bill_name, text="Total", font='Courier 10 bold', bg='dark blue', fg='white', bd=7, width='10',
                   command=total)
total_btn.grid(row=1, column=5, pady=10, padx=9)

bill_btn = Button(Bill_name, text="Generate Bill", font='Courier 10 bold', bg='dark blue', fg='white', bd=7, width='12',
                  command=billarea)
bill_btn.grid(row=1, column=6, pady=10, padx=9)

clear_btn = Button(Bill_name, text="Clear", font='Courier 10 bold', bg='dark blue', fg='white', bd=7, width='10',
                   command=clear_file)
clear_btn.grid(row=1, column=7, pady=10, padx=9)

exit_btn = Button(Bill_name, text="Exit", font='Courier 10 bold', bg='dark blue', fg='white', bd=7, width='8',
                  command=exit_screen)
exit_btn.grid(row=1, column=8, pady=10, padx=9)

root.mainloop()
