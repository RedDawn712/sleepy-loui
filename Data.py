import re
from tkinter import messagebox

#Bike types


#Button click function
def button_clicked(txt_first_name1, txt_last_name1, txt_address1,
                   txt_zipcode1, txt_email1, txt_mobilenr1):
    if (not txt_first_name1.get().strip()
            or not txt_last_name1.get().strip()
            or not txt_address1.get().strip()
            or not txt_zipcode1.get().strip()
            or not txt_email1.get().strip()
            or not txt_mobilenr1.get().strip()):

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

