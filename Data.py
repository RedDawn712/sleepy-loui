import re
from tkinter import messagebox


#Button click function
def button_clicked(txt_first_name, txt_last_name, txt_address,
                   txt_zipcode, txt_email, txt_mobilenr):
    if (not txt_first_name.get().strip()
            or not txt_last_name.get().strip()
            or not txt_address.get().strip()
            or not txt_zipcode.get().strip()
            or not txt_email.get().strip()
            or not txt_mobilenr.get().strip()):

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

