from tkinter import *
from PIL import ImageTk, Image
import os

root=Tk()
root.title("Check Buttons")

opcion1 = IntVar()
opcion2 = IntVar()
opcion3 = IntVar()

def opciones():
    opciones_seleccionadas=""
    if opcion1.get() == 1:
        opciones_seleccionadas += " Opción 1."
    if opcion2.get() == 1:
        opciones_seleccionadas += " Opción 2."
    if opcion3.get() == 1:
        opciones_seleccionadas += " Opción 3."
    
    mostrar_opciones.config(text=opciones_seleccionadas)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
imagen = PhotoImage(file="fym1.PNG")
Label(root, image=imagen).pack()


frame0=Frame(root)
frame0.pack()

Label(frame0, text="Selección múltiple:",width=50).pack()

Checkbutton(frame0, text="Opción 1", variable=opcion1, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(frame0, text="Opción 2", variable=opcion2, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(frame0, text="Opción 3", variable=opcion3, onvalue=1, offvalue=0, command=opciones).pack()

mostrar_opciones=Label(frame0)
mostrar_opciones.pack()

root.mainloop()
