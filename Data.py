import ttkbootstrap

#Persoonsgegevens data
class Persoonsgegevens:
        def __init__(self, voornaam, achternaam, adres, postcode):
            self.voornaam = voornaam
            self.achternaam = achternaam
            self.adres = adres
            self.postcode = postcode

#Button click
def button_clicked():
    if(not txt_voornaam.get().strip() or
    not txt_achternaam.get().strip() or
    not txt_adres.get().strip() or
    not txt_postcode.get().strip() or
    not txt_email.get().strip()):
        messagebox.showerror(title= "Ontbrekende gegevens", message= "Vul allen velden in")
    else:
        messagebox.showinfo(title= "Succes!", message= "Reservering verstuurd!")



