from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


import Data

root = Tk()

root.title("Fietsreservering bij Biker")
root.geometry('1024x768')

lbl = Label(root, text= "Bij Biker kom je vooruit.")
lbl.grid()
persoonsgegevens= Data.Persoonsgegevens("",'" ', "", "" )

#Persoonsgegevens invullen
def persoonsgegevens():
    lbl1 = Label(root, text= "Persoonsgegevens")
    lbl1.grid(row= 2, column= 0)
    lbl2 = Label(root, text= "Voornaam")
    lbl2.grid(row=3, column=0)
    txt = Entry(root, width= 15)
    txt.grid(row= 3, column=1)
    lbl3 = Label(root, text= "Achternaam")
    lbl3.grid(row=4, column=0)
    txt1 = Entry(root, width= 15)
    txt1.grid(row= 4, column=1)
    lbl4 = Label(root, text= "Adres")
    lbl4.grid(row=5, column=0)
    txt2 = Entry(root, width= 15)
    txt2.grid(row= 5, column=1)
    lbl5 = Label(root, text= "Postcode")
    lbl5.grid(row=6, column=0)
    txt3 = Entry(root, width= 15)
    txt3.grid(row= 6, column=1)

def button_clicked():
    print("Reservering is verstuurd")
Button(root, text= "Reservering versturen", command=button_clicked)
Button.pack(side = 'bottom')

if not persoonsgegevens():
    messagebox.showerror(title= "Ontbrekende gegevens", message= "Vull alle gegevens in om de reservering af te ronden")

root.mainloop()