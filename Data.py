import re
from tkinter import messagebox
import tkinter as tk

#Button click function
def button_clicked(txt_voornaam, txt_achternaam, txt_adres,
                   txt_postcode, txt_email, txt_telefoonnr):
    if (not txt_voornaam.get().strip()
            or not txt_achternaam.get().strip()
            or not txt_adres.get().strip()
            or not txt_postcode.get().strip()
            or not txt_email.get().strip()
            or not txt_telefoonnr.get().strip()):

        messagebox.showerror(title="Ontbrekende gegevens", message="Vul alle velden in")
    else:
        messagebox.showinfo(title="Succes!", message="Reservering verstuurd!")


#Maximum len postcode
postcode_re = re.compile(r'^(?:\d{0,4}|\d{4}[A-Z]{0,2})$')

def validate_postcode(text):
    text = text.upper()
    if not postcode_re.match(text):
        return False
    return True