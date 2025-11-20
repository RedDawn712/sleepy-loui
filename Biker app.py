from Data import *
from tkinter import *
import tkinter as tk

root = Tk()
root.title("Fietsreservering bij Biker")
root.geometry('1024x768')

lblslogan = Label(root, text= "Bij Biker kom je vooruit.")
lblslogan.grid()


#Entry velden
Label(root, text= "Persoonsgegevens").grid(row= 2, column= 0)

Label(root, text= "Voornaam").grid(row=3, column=0)
txt_voornaam = Entry(root, width= 20)
txt_voornaam.grid(row= 3, column=1)

Label(root, text= "Achternaam").grid(row=4, column=0)
txt_achternaam = Entry(root, width= 20)
txt_achternaam.grid(row= 4, column=1)

Label(root, text= "Adres").grid(row=5, column=0)
txt_adres = Entry(root, width= 20)
txt_adres.grid(row= 5, column=1)

Label(root, text= "Postcode").grid(row=6, column=0)
vcmd = (root.register(validate_postcode), '%P')
txt_postcode = tk.Entry(root, width=20, validate='key', validatecommand=vcmd)
txt_postcode.grid(row=6, column=1)


Label(root, text="E-mail adres").grid(row=7, column=0)
txt_email = Entry(root, width=20)
txt_email.grid(row=7, column=1)

lbltelefoonnr = Label(root, text="Telefoon nummer").grid(row=8, column=0)
txt_telefoonnr = Entry(root, width=20)
txt_telefoonnr.grid(row=8, column=1)


#Button reservering verzenden
Button = Button(root,
                text="Reservering versturen",
                command= lambda: button_clicked(txt_voornaam, txt_achternaam, txt_adres, txt_postcode, txt_email, txt_telefoonnr))
Button.grid(row=15, column=15)

root.mainloop()