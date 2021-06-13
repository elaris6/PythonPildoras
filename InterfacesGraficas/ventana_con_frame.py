from tkinter import *

"""
Para que la aplicación no se abra con la consola detrás, el script de python debe tener extensión "pyw", en lugar de "py"
"""

raiz=Tk()

raiz.title("Ventana de pruebas")

# raiz.iconbitmap("ruta_imagen '.ico' ") # El nombre es importante porque se utilizará para el nombre del empaquetado de la aplicación

#raiz.geometry("640x480") # Si no se especifica, se adapta al tamaño del frame

raiz.resizable(1,1) # (width, height) Habilita o bloquea la posibilidad de redimensión manual. Por defecto el valor es 1 ó True

raiz.config(bg="grey")

# Construimos un frame y le damos algo de configuración
unFrame=Frame() 

#unFrame.pack(side="left",anchor="n")

unFrame.pack(fill="y",expand="True")

unFrame.config(width="640",height="480")

unFrame.config(bg="lightgrey")

# Configurar ancho y tipo de borde para el frame
unFrame.config(bd=20)
unFrame.config(relief="groove")

# Otras muchas opciones de configuración
unFrame.config(cursor="hand2")

#Siempre al final
raiz.mainloop() # Bucle infinito de ejecución de la ventana para mantenerla a la escucha

