from tkinter import *
import os

"""
Para que la aplicación no se abra con la consola detrás, el script de python debe tener extensión "pyw", en lugar de "py"
"""
os.chdir(os.path.dirname(os.path.abspath(__file__)))

root=Tk()

root.title("Prueba de labels")

frame1=Frame(root,width="320",height="240",bg="lightgrey")
frame1.pack()

label1_frame=Label(frame1,text="Texto label frame",fg="blue",font=("Comic Sans MS",18))
label1_frame.place(x="5",y="5")

# Otra opción mejor si no se va a reutilizar el label es:
# Label(root,text="texto label raiz").place(x="5",y="5")


# Creamos otro frame y utilizamos el label para cargar una imagen

frame2=Frame(root,width="320",height="240",bg="grey")
frame2.pack()

imagen_frame = PhotoImage(file="fym1.PNG")
Label(frame2,image=imagen_frame).place(x="0",y="0")


#Siempre al final
root.mainloop() # Bucle infinito de ejecución de la ventana para mantenerla a la escucha
