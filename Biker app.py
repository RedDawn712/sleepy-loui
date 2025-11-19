import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import Data
from Data import *

root = Tk()

root.title("Fietsreservering bij Biker")
root.geometry('1024x768')

lbl = Label(root, text= "Bij Biker kom je vooruit.")
lbl.grid()
persoonsgegevens= Data.Persoonsgegevens("",'" ', "", "" )

#Variabelen Entry-velden
txt_voornaam= None
txt_achternaam = None
txt_adres= None
txt_postcode= None
txt_email= None


#Persoonsgegevens invullen
def persoonsgegevens():
    global txt_voornaam, txt_achternaam, txt_adres, txt_postcode, txt_email

    lbl1 = Label(root, text= "Persoonsgegevens").grid(row= 2, column= 0)

    lbl2 = Label(root, text= "Voornaam").grid(row=3, column=0)
    txt_voornaam = Entry(root, width= 15)
    txt_voornaam.grid(row= 3, column=1)

    lbl3 = Label(root, text= "Achternaam").grid(row=4, column=0)
    txt_achternaam = Entry(root, width= 15)
    txt_achternaam.grid(row= 4, column=1)

    lbl4 = Label(root, text= "Adres").grid(row=5, column=0)
    txt_adres = Entry(root, width= 15)
    txt_adres.grid(row= 5, column=1)

    lbl5 = Label(root, text= "Postcode").grid(row=6, column=0)
    txt_postcode = Entry(root, width= 15)
    txt_postcode.grid(row= 6, column=1)

    lbl6 = Label(root, text="E-mail adres").grid(row=7, column=0)
    txt_email = Entry(root, width=15)
    txt_email.grid(row=7, column=1)




def button_clicked():
    if(not txt_voornaam.get().strip() or
    not txt_achternaam.get().strip() or
    not txt_adres.get().strip() or
    not txt_postcode.get().strip() or
    not txt_email.get().strip()):
        messagebox.showerror(title= "Ontbrekende gegevens", message= "Vul allen velden in")
    else:
        messagebox.showinfo(title= "Succes!", message= "Reservering verstuurd!")

Button = Button(root,
                text="Reservering versturen",
                command=button_clicked)
Button.grid(row=15, column=15)

persoonsgegevens()

root.mainloop()