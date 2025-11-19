import re
import ttkbootstrap
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk



#Button click function
def button_clicked():
    if not txt_voornaam.get().strip() or not txt_achternaam.get().strip() or not txt_adres.get().strip() or not txt_postcode.get().strip() or not txt_email.get().strip() or not txt_telefoonnr.get().strip():
        messagebox.showerror(title="Ontbrekende gegevens", message="Vul alle velden in")
    else:
        messagebox.showinfo(title="Succes!", message="Reservering verstuurd!")


#Maximum len postcode
postcode_re = re.compile(r'^(?:\d{0,4}|\d{4}[A-Z]{0,2})$')

def validate_postcode(text):
    text = text.upper()
    if not postcode_re.match(text):
        return False
    try:
        txt_postcode.delete(0, tk.END)
        txt_postcode.insert(0, text)
        txt_postcode.icursor(len(text))
    except Exception:
        pass
    return True

#Txt names
def persoonsgegevens():
    global txt_voornaam, txt_achternaam, txt_adres, txt_postcode, txt_email, txt_telefoonnr


#Variabelen Entry-velden
txt_voornaam = None
txt_achternaam = None
txt_adres = None
txt_postcode = None
txt_email = None
txt_telefoonnr = None
