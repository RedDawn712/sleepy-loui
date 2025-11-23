import ttkbootstrap
from tkinter.ttk import *
from Data import *
from tkinter import *
import tkinter as tk
from Data import create_placeholder

#Start window
root = tk.Tk()
root.title("Biker fietsverhuur")
root.geometry('500x500')

#3 column configure
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

#start window slogan
lblslogan = Label(root, text= "Met Biker kom je vooruit.", font=("Arial", 14))
lblslogan.grid(row=0, column=1)

# Bottom header
footer = Label(root,
               text="© 2025 Biker Fietsverhuur",
               bg="grey",
               fg="white",
               font=("Arial", 12))

footer.place(relx=0, rely=1.0, anchor='sw', relwidth=1)

#Reservation window
def open_new_window():
    reservation_window = Toplevel(root)
    reservation_window.title("Fiets Reserveren")
    reservation_window.geometry('500x500')
    root.iconify() #After opening new window, main window minimizes

    Label(reservation_window, text= "Vul je gegevens in").grid()

    # Header text
    Label(reservation_window,
          text="Biker Fietsreservering",
          bg='grey',
          fg='white',
          font=("Arial", 15)).place(relx=0.5, y=10., anchor= 'n')
    Label(reservation_window, text="Persoonsgegevens").grid(row=2,
                                                            column=0)
    #Entry fields reservation
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
    txt_zipcode1 = tk.Entry(reservation_window,
                            width=20,
                            validate='key',
                            validatecommand=vcmd1)
    txt_zipcode1.grid(row=6, column=1)

    Label(reservation_window, text="E-mail adres").grid(row=7, column=0)
    txt_email1 = Entry(reservation_window, width=20)
    txt_email1.grid(row=7, column=1)

    Label(reservation_window, text="Telefoon nummer").grid(row=8, column=0)
    txt_mobilenr1 = Entry(reservation_window, width=20)
    txt_mobilenr1.grid(row=8, column=1)

    Label(reservation_window, text= "Kies een soort fiets").grid(row=9, column=0)

    #Dropdownbox creation
    n = tk.StringVar()
    bike_type = ttkbootstrap.Combobox(reservation_window, width= 20, textvariable= n,)

    #Addig bike types
    bike_type['values'] = ('Dames fiets',
                           'Heren fiets',
                           'Elektrische fiets',
                           'Mountainbike',
                           'Kinderfiets')
    bike_type.grid(row=9, column=1)

    #Payment method creation
    v= StringVar(reservation_window, "1")
    values= {"iDeal": "1",
             "Creditcard": "2",
             "Overschrijven": "3",
             "Paypal": "4"}
    v.set("1")

    for i, (text, value) in enumerate(values.items()):
        Radiobutton(reservation_window,
                    text=text,
                    variable=v,
                    value=value).grid(row=10 + i, column=1, sticky= "w", pady=2)


    # Button send reservation
    send_button =Button(reservation_window,
                    text="Reservering versturen",
                    command=lambda: button_clicked(txt_first_name1,
                                                   txt_last_name1,
                                                   txt_address1,
                                                   txt_zipcode1,
                                                   txt_email1,
                                                   txt_mobilenr1,
                                                   bike_type))

    send_button.grid(row=16, column=1, columnspan=2, pady=10)

#Damesfiets placeholder
ph_dames = (create_placeholder(root, "Damesfiets"))
ph_dames.grid(row=2, column= 0, pady=15)
Button(root, text= "Reserveer nu!", command= open_new_window).grid(row=3, column=0)

#Herenfiets placeholder
ph_heren=(create_placeholder(root, text="Herenfiets"))
ph_heren.grid(row=2, column= 1, pady=15)
Button(root, text= "Reserveer nu!", command= open_new_window).grid(row= 3, column= 1)

#Elektrische fiets placeholder
ph_elektrisch=(create_placeholder(root, text="Elektrische fiets"))
ph_elektrisch.grid(row=2, column=2, pady=15)
Button(root, text="Reserveer nu!", command= open_new_window).grid(row=3, column= 2)



#Worker login page
def worker_login():
    worker_window = Toplevel(root)
    worker_window.title("Medewerker Inloggen")
    worker_window.geometry('500x500')
    root.iconify() #Closes mainwindow

    #Worker login entry fields
    Label(worker_window, text="Gebruikersnaam").grid(row=4, column=0)
    Label(worker_window, text="Wachtwoord").grid(row=5, column=0)
    txt_username= Entry(worker_window, width=20)
    txt_username.grid(row=4, column=1)
    txt_password = Entry(worker_window, width=20)
    txt_password.grid(row=5, column=1)

    #Worker login button
    Button(worker_window, text="Login", command= open_new_window).grid(row=6, column= 1)

#Worker inlogpage button
Button(root,
       text="Medewerker inloggen",
       command=worker_login).place(rely=0.95, relx=1, anchor="se")


root.mainloop()