import ttkbootstrap
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


#Persoonsgegevens Class
class CLASSPersoonsgegevens:
        def __init__(self, voornaam, achternaam, adres, postcode):
            self.voornaam = voornaam
            self.achternaam = achternaam
            self.adres = adres
            self.postcode = postcode

#Button click function
def button_clicked():
    if(not txt_voornaam.get().strip() or
    not txt_achternaam.get().strip() or
    not txt_adres.get().strip() or
    not txt_postcode.get().strip() or
    not txt_email.get().strip() or
    not txt_telefoonnr.get().strip()):
        messagebox.showerror(title= "Ontbrekende gegevens", message= "Vul alle velden in")
    else:
        messagebox.showinfo(title= "Succes!", message= "Reservering verstuurd!")

#Maximum len postcode
def validate_postcode(text, new_text):
    if len(new_text) >6:
        return False
    return text.isdecimal()

def persoonsgegevens():
    global txt_voornaam, txt_achternaam, txt_adres, txt_postcode, txt_email, txt_telefoonnr

#Variabelen Entry-velden
txt_voornaam= None
txt_achternaam = None
txt_adres= None
txt_postcode= None
txt_email= None
txt_telefoonnr= None