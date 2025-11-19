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

lblslogan = Label(root, text= "Bij Biker kom je vooruit.")
lblslogan.grid()


#Persoonsgegevens invullen
lblpersoonsgegevens = Label(root, text= "Persoonsgegevens").grid(row= 2, column= 0)

lblvoornaam = Label(root, text= "Voornaam").grid(row=3, column=0)
txt_voornaam = Entry(root, width= 15)
txt_voornaam.grid(row= 3, column=1)

lblachternaam = Label(root, text= "Achternaam").grid(row=4, column=0)
txt_achternaam = Entry(root, width= 15)
txt_achternaam.grid(row= 4, column=1)

lbladres = Label(root, text= "Adres").grid(row=5, column=0)
txt_adres = Entry(root, width= 15)
txt_adres.grid(row= 5, column=1)

lblpostcode = Label(root, text= "Postcode").grid(row=6, column=0)
txt_postcode = Entry(root, width= 15, validate = "key", validatecommand= (root.register(validate_postcode), "%S", "%P"))
txt_postcode.grid(row= 6, column=1)

lblemail = Label(root, text="E-mail adres").grid(row=7, column=0)
txt_email = Entry(root, width=15)
txt_email.grid(row=7, column=1)

lbltelefoonnr = Label(root, text="Telefoon nummer").grid(row=8, column=0)
txt_telefoonnr = Entry(root, width=15)
txt_telefoonnr.grid(row=8, column=1)

Button = Button(root,
                text="Reservering versturen",
                command=button_clicked)
Button.grid(row=15, column=15)

persoonsgegevens()

root.mainloop()