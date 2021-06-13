from tkinter import *
from PIL import ImageTk, Image
import os

"""
Para que la aplicación no se abra con la consola detrás, el script de python debe tener extensión "pyw", en lugar de "py"
"""

raiz=Tk()

raiz.title("Ventana de pruebas")

#raiz.iconbitmap(r".\\emoji.ico") # El nombre es importante porque se utilizará para el nombre del empaquetado de la aplicación
raiz.call('wm', 'iconphoto', raiz._w, ImageTk.PhotoImage(Image.open(os.path.dirname(__file__)+'/py_calc.ico')))

raiz.geometry("640x480")

raiz.resizable(1,1) # (width, height) Habilita o bloquea la posibilidad de redimensión manual. Por defecto el valor es 1 ó True

raiz.config(bg="blue")

#Siempre al final
raiz.mainloop() # Bucle infinito de ejecución de la ventana para mantenerla a la escucha

