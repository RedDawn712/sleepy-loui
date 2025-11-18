from tkinter import *

root = Tk()

root.title("Welkom bij Biker")
root.geometry('1024x768')

lbl = Label(root, text= "Bij Biker kom je vooruit.")
lbl.grid()

lbl1 = Label(root, text= "Persoonsgegevens")
lbl1.grid(row= 2, column= 0)
lbl2 = Label(root, text= "Voornaam")
lbl2.grid(row=2, column=1)
txt = Entry(root, width= 15)
txt.grid(row= 3, column=1)

mainloop()