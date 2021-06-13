# Creando menús, submenús y submenús anidados

from tkinter import *

root=Tk()
root.title("Aprendiendo con los menús")

# Creamos elemento menú principal
barraMenu=Menu(root)
root.config(menu=barraMenu,width=500,height=300)

# Creamos un elemento de opción de manú principal
opcion1Menu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Opción 1", menu=opcion1Menu)
# Creamos un elemento menú asociado a un elemeno de menú principal. Esto es un elemento submenú
opcion1Submenu=Menu(opcion1Menu,tearoff=0)
opcion1Menu.add_cascade(label="Subopción 1.1",menu=opcion1Submenu)
# Creamos elementos finales del submenú
opcion1Submenu.add_command(label="Subopción 1.1.1")
opcion1Submenu.add_command(label="Subopción 1.1.2")
# Creamos elementos finales de la opción principal de menú
opcion1Menu.add_command(label="Subopción 1.2")
opcion1Menu.add_command(label="Subopción 1.3")
opcion1Menu.add_separator() # Separador entre elemenos de menú
opcion1Menu.add_command(label="Subopción 1.4")
opcion1Menu.add_command(label="Subopción 1.5")

opcion2Menu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Opción 2", menu=opcion2Menu)
opcion2Menu.add_command(label="Subopción 2.1")
opcion2Submenu = Menu(opcion2Menu,tearoff=0)
opcion2Menu.add_cascade(label="Subopción 2.2", menu=opcion2Submenu)
opcion2Submenu.add_command(label="Subopción 2.1.1")
opcion2Submenu.add_command(label="Subopción 2.1.2")
opcion2Submenu.add_command(label="Subopción 2.1.3")

opcion3Menu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Opción 3", menu=opcion3Menu)
opcion3Menu.add_command(label="Subopción 3.1")
opcion3Menu.add_command(label="Subopción 3.2")
opcion3Menu.add_separator()
opcion3Menu.add_command(label="Subopción 3.3")
opcion3Menu.add_command(label="Subopción 3.4")
opcion3Menu.add_command(label="Subopción 3.5")
opcion3Menu.add_separator()
opcion3Menu.add_command(label="Subopción 3.6")
opcion3Menu.add_command(label="Subopción 3.7")

opcion4Menu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Opción 4", menu=opcion4Menu)
opcion4Menu.add_command(label="Subopción 4.1")


root.mainloop()
