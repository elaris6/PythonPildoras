from tkinter import *

root=Tk()
root.title("Titulo ventana")

#root.geometry("640x480")
frame1=Frame(root,width="640",height="480",bg="grey")
frame1.pack()


cuadroTexto1=Entry(frame1,bg="lightgrey")
cuadroTexto1.grid(row="0",column="1",pady=5,padx=5)
label1=Label(frame1, text="Nombre:")
label1.grid(row="0",column="0",sticky="e",pady=5,padx=5)

cuadroTexto2=Entry(frame1,bg="lightgrey")
cuadroTexto2.grid(row="1",column="1",pady=5,padx=5)
label2=Label(frame1, text="Apellido:")
label2.grid(row="1",column="0",sticky="e",pady=5,padx=5)

cuadroTexto3=Entry(frame1,bg="lightgrey")
cuadroTexto3.grid(row="2",column="1",pady=5,padx=5)
label3=Label(frame1, text="Edad:")
label3.grid(row="2",column="0",sticky="e",pady=5,padx=5)

cuadroTexto4=Entry(frame1,bg="lightgrey")
cuadroTexto4.grid(row="3",column="1",pady=5,padx=5)
label4=Label(frame1, text="Usuario:")
label4.grid(row="3",column="0",sticky="e",pady=5,padx=5)

cuadroTexto5=Entry(frame1,bg="orange")
cuadroTexto5.grid(row="4",column="1",pady=5,padx=5)
cuadroTexto5.config(show="*")
label5=Label(frame1, text="Password:")
label5.grid(row="4",column="0",sticky="e",pady=5,padx=5)

root.mainloop()