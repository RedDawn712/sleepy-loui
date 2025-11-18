from tkinter import *

root = Tk()

root.title("Welkom bij Biker")
root.geometry('1024x768')

lbl = Label(root, text = "Wil je een fiets huren?")
lbl.grid()
txt = Entry(root, width=10)
txt.grid(column=1, row=0)

def clicked():
    res = "you wrote "+ txt.get()
    lbl.configure(text=res)


btn = Button(root, text="Klik op mij", fg="red", command=clicked)
btn.grid(column=2, row=0)
root.mainloop()