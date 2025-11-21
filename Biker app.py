from Data import *
from tkinter import *
import tkinter as tk
from tkinter.ttk import *

#Start window
root = Tk()
root.title("Biker fietsverhuur")
root.geometry('1200x800')
lblslogan = Label(root, text= "Bij Biker kom je vooruit.")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
lblslogan.grid(row=0, column=1)



#Start window Top
Label(root, text= "Beschikbare fietsen").grid(row= 2, column= 0)

Label(root, text= "Damesfietsen").grid(row=3, column=0)
txt_ladies_bike = Entry(root, width= 20)
txt_ladies_bike.grid(row= 3, column=1)

Label(root, text= "Herenfietsen").grid(row=4, column=0)
txt_mens_bike = Entry(root, width= 20)
txt_mens_bike.grid(row= 4, column=1)

Label(root, text= "Elektrische fietsen").grid(row=5, column=0)
txt_electric_bike = Entry(root, width= 20)
txt_electric_bike.grid(row= 5, column=1)

Label(root, text= "Mountainbikes").grid(row=6, column=0)
txt_mountainbike = tk.Entry(root, width=20,)
txt_mountainbike.grid(row=6, column=1)

Label(root, text="Accessoires").grid(row=7, column=0)
txt_accesoires = Entry(root, width=20)
txt_accesoires.grid(row=7, column=1)

#Reservation window
def open_new_window():
    reservation_window = Toplevel(root)
    reservation_window.title("Fiets Reserveren")
    reservation_window.geometry('1024x768')
    root.iconify() #After opening new window, main window minimizes
    Label(reservation_window, text= "Hier kan je reserveren").grid()

    # Entry field reservation
    Label(reservation_window, text="Persoonsgegevens").grid(row=2, column=0)

    Label(reservation_window, text="Voornaam").grid(row=3, column=0)
    txt_first_name1 = Entry(reservation_window, width=20)
    txt_first_name1.grid(row=3, column=1)

    Label(reservation_window, text="Achternaam").grid(row=4, column=0)
    txt_last_name1 = Entry(reservation_window, width=20)
    txt_last_name1.grid(row=4, column=1)

    Label(reservation_window, text="Adres").grid(row=5, column=0)
    txt_address1 = Entry(reservation_window, width=20)
    txt_address1.grid(row=5, column=1)

    Label(reservation_window, text="Postcode").grid(row=6, column=0)
    vcmd1 = (reservation_window.register(validate_zipcode), '%P')
    txt_zipcode1 = tk.Entry(reservation_window, width=20, validate='key', validatecommand=vcmd1)
    txt_zipcode1.grid(row=6, column=1)

    Label(reservation_window, text="E-mail adres").grid(row=7, column=0)
    txt_email1 = Entry(reservation_window, width=20)
    txt_email1.grid(row=7, column=1)

    Label(reservation_window, text="Telefoon nummer").grid(row=8, column=0)
    txt_mobilenr1 = Entry(reservation_window, width=20)
    txt_mobilenr1.grid(row=8, column=1)

    # Button send reservation
    send_button =Button(reservation_window,
                    text="Reservering versturen",
                    command=lambda: button_clicked(txt_first_name1,
                                                   txt_last_name1,
                                                   txt_address1,
                                                   txt_zipcode1,
                                                   txt_email1,
                                                   txt_mobilenr1))
    send_button.grid(row=15, column=15)

#Reservation page button
Button(root, text= "Fiets reserveren", command= open_new_window).grid()

#Worker inlogpage button
Button(root, text=("Medewerker inloggen")).grid(row=100, column=800)

root.mainloop()