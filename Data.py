import re
from tkinter import messagebox
import ttkbootstrap
from tkinter.ttk import *
from Data import *
from tkinter import *
import tkinter as tk
#Main window frame
def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)


#Placeholder maker
def create_placeholder(parent, text):
    canvas= tk.Canvas(parent,
                      width=120,
                      height=90,
                      bg='grey',
                      highlightthickness=1,
                      highlightbackground='black')
    canvas.create_text(60, 45, text=text)
    return canvas



#Button click function reservation
def button_clicked(txt_first_name1, txt_last_name1, txt_address1,
                   txt_zipcode1, txt_email1, txt_mobilenr1, bike_type):
    if (not txt_first_name1.get().strip()
            or not txt_last_name1.get().strip()
            or not txt_address1.get().strip()
            or not txt_zipcode1.get().strip()
            or not txt_email1.get().strip()
            or not txt_mobilenr1.get().strip()
            or not bike_type.get()):

        messagebox.showerror(title="Ontbrekende gegevens", message="Vul alle velden in")

    else:
        messagebox.showinfo(title="Succes!", message="Reservering verstuurd!")



#Maximum length zipcode
zipcode_re = re.compile(r'^(?:\d{0,4}|\d{4}[A-Z]{0,2})$')

def validate_zipcode(text):
    text = text.upper()
    if not zipcode_re.match(text):
        return False
    return True
