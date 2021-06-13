from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = ""  # La utilizaremos para almacenar la ruta del fichero


def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""  # Reiniciamos la ruta
    texto.delete(1.0, "end")  # En flotante, el primer carácter es un salto
    root.title("Mi editor")  # Reiniciamos el título


def abrir():
    # Indicamos que la ruta es respecto a la variable global
    # Debemos de forzar esta lectura global porque los comandos
    # sólo son conscientes de las variables externas que son widgets

    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(("Ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto")

    # Si la ruta es válida abrimos el contenido en lectura
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')  # Nos aseguramos de que esté vacío
        texto.insert('insert', contenido)  # Le insertamos el contenido
        fichero.close()  # Cerramos el fichero
        root.title(ruta + " - Mi editor")  # Cambiamos el título


def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')  # Recuperamos el texto
        fichero = open(ruta, 'w+')  # Creamos el fichero o abrimos
        fichero.write(contenido)  # Escribimos el texto
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardar_como()


def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")

    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")

    if fichero is not None:
        ruta = fichero.name  # El atributo name es la ruta, si está abierto
        contenido = texto.get(1.0, 'end-1c')  # recuperamos el texto
        fichero = open(ruta, 'w+')  # creamos el fichero o abrimos
        fichero.write(contenido)  # escribimos el texto
        fichero.close()
        mensaje.set("Fichero guardado correctamente") # Actualizamos mensaje
    else:
        mensaje.set("Guardado cancelado")  # Actualizamos mensaje
        ruta = "" # Reiniciamos ruta


# Configuración de la raíz
root = Tk()
root.title("Mi editor")

# Menú superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side="left")

root.config(menu=menubar)
# Finalmente bucle de la apliación
root.mainloop()
