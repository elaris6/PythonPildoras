from tkinter import *

root=Tk()
root.title("Titulo ventana")

#root.geometry("640x480")
frame1=Frame(root,width="640",height="480",bg="grey")
frame1.pack()

usuario=StringVar()
label1=Label(frame1, text="Usuario:")
label1.grid(row="0",column="0",sticky="e",pady=5,padx=5)
cuadroTexto1=Entry(frame1,bg="lightgrey",textvariable=usuario)
cuadroTexto1.grid(row="0",column="1",pady=5,padx=5)

password=StringVar()
label2=Label(frame1, text="Password:")
label2.grid(row="1",column="0",sticky="e",pady=5,padx=5)
cuadroTexto2=Entry(frame1,bg="orange",textvariable=password)
cuadroTexto2.grid(row="1",column="1",pady=5,padx=5)
cuadroTexto2.config(show="*")

label3=Label(frame1, text="Texto libre:")
label3.grid(row="2",column="0",sticky="e",pady=5,padx=5)
text3=Text(frame1,width="20",height="5")
text3.grid(row="2",column="1",pady="5",padx="5")
scroll3=Scrollbar(frame1,command=text3.yview)
scroll3.grid(row="2",column="2",sticky="nsew")
text3.config(yscrollcommand=scroll3.set)

def codigoBoton():
    usuario.set("user usuario userito")
    password.set("Introducte contraseña!!!")

botonPrueba=Button(root,text="Prueba",command=codigoBoton)
botonPrueba.pack()



root.mainloop()