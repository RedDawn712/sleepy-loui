from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap
import tkinter as tk
import Data
from Biker.Data import button_clicked

root = Tk()

root.title("Fietsreservering bij Biker")
root.geometry('1024x768')

lbl = Label(root, text= "Bij Biker kom je vooruit.")
lbl.grid()
persoonsgegevens= Data.Persoonsgegevens("", "", "", "")

#Persoonsgegevens invullen
def gegevens_velden():
    lbl1 = Label(root, text="Persoonsgegevens")
    lbl1.grid(row=2, column=0)

    voornaam_entry = tk.Label(root, text= "Voornaam")
    voornaam_entry.grid(row=3, column=0)
    txt = Entry(root, width=15)
    txt.grid(row=3, column=1)

    lbl3 = Label(root, text="Achternaam")
    lbl3.grid(row=4, column=0)
    txt1 = Entry(root, width=15)
    txt1.grid(row=4, column=1)

    lbl4 = Label(root, text="Adres")
    lbl4.grid(row=5, column=0)
    txt2 = Entry(root, width=15)
    txt2.grid(row=5, column=1)

    lbl5 = Label(root, text="Postcode")
    lbl5.grid(row=6, column=0)
    txt3 = Entry(root, width=15)
    txt3.grid(row=6, column=1)
gegevens_velden()

Button = tk.Button(root, command=button_clicked(), text= "Reservering verzenden")
Button.grid_configure()

root.mainloop()