from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Prácticas con interfaces")

def abrirFichero():
    fichero = filedialog.askopenfilename(title="Aprendiendo a abrir archivos", initialdir="C:\\Users\\elaris6\Desktop\\Practicas_Python\\",filetypes=(("Scripts de Python","*.py"),("Ficheros de texto","*.txt"),("Todos los ficheros","*.*")))
    print(fichero)

def guardarFichero():
    fichero = filedialog.asksaveasfile(
        title="Guardar un fichero", mode='w', defaultextension=".txt")

    if fichero is not None:
        fichero.write("Holita")
        fichero.close()

def informacion():
    messagebox.showinfo("Titulo Ventana","Mensaje a mostrar en el messagebox")

def alerta():
    messagebox.showwarning("Titulo Ventana", "Mensaje a mostrar en el messagebox")

def error():
    messagebox.showerror("Titulo Ventana", "Mensaje a mostrar en el messagebox")

def salirAplicacion():
    valor=messagebox.askokcancel("Titulo ventana","Quieres salir?",parent=root)
    if valor==True:
        root.destroy()

def cerrarProceso():
    valor=messagebox.askretrycancel("Título","Quieres cerrar el proceso actual")
    if valor == True:
        salirAplicacion()
    

barraMenu = Menu(root)
root.config(menu=barraMenu, width=500, height=300)

opcion1Menu = Menu(barraMenu, tearoff=0)
opcion1Menu.add_command(label="Abrir archivo",command=abrirFichero)
opcion1Menu.add_command(label="Guardar archivo", command=guardarFichero)
opcion1Menu.add_command(label="Subopción 1.3")
opcion1Menu.add_separator()
opcion1Menu.add_command(label="Cerrar proceso",command=cerrarProceso)
opcion1Menu.add_command(label="Salir",command=salirAplicacion)


opcion2Menu = Menu(barraMenu, tearoff=0)
opcion2Menu.add_command(label="Subopción 2.1")
opcion2Submenu = Menu(opcion2Menu, tearoff=0)
opcion2Menu.add_cascade(label="Subopción 2.2", menu=opcion2Submenu)
opcion2Submenu.add_command(label="Subopción 2.1.1")
opcion2Submenu.add_command(label="Subopción 2.1.2")
opcion2Submenu.add_command(label="Subopción 2.1.3")

opcion3Menu = Menu(barraMenu, tearoff=0)
opcion3Menu.add_command(label="Subopción 3.1")
opcion3Menu.add_separator()
opcion3Menu.add_command(label="Subopción 3.2")

opcion4Menu = Menu(barraMenu, tearoff=0)
opcion4Menu.add_command(label="Mostrar información",command=informacion)
opcion4Menu.add_command(label="Mostrar alerta", command=alerta)
opcion4Menu.add_command(label="Mostrar error", command=error)

barraMenu.add_cascade(label="Opción 1", menu=opcion1Menu)

barraMenu.add_cascade(label="Opción 2", menu=opcion2Menu)

barraMenu.add_cascade(label="Opción 3", menu=opcion3Menu)

barraMenu.add_cascade(label="Ventanas emergentes", menu=opcion4Menu)

root.mainloop()
