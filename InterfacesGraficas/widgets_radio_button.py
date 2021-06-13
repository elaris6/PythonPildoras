# Widgets radio buttons

from tkinter import *

root=Tk()

var_opcion=IntVar()

def imprimir_opcion():
    #print("La opción elegida es: "+str(var_opcion.get()))
    if var_opcion.get()==1:
        etiqueta.config(text="La opción elegida es: 1")
    elif var_opcion.get()==2:
        etiqueta.config(text="La opción elegida es: 2")
    elif var_opcion.get() == 3:
        etiqueta.config(text="La opción elegida es: 3")

Label(root,text="Selección excluyente:").pack()

Radiobutton(root, text="Opción1", variable=var_opcion, value=1, command=imprimir_opcion).pack()
Radiobutton(root, text="Opción2", variable=var_opcion, value=2, command=imprimir_opcion).pack()
Radiobutton(root, text="Opción3", variable=var_opcion,
            value=3, command=imprimir_opcion).pack()
etiqueta=Label(root)
etiqueta.pack()

root.mainloop()
