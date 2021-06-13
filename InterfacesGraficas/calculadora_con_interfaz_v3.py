# Calculadora con interfaz gráfica
# v3. Eliminamos variable global operando1 e implementamos pantallas secundarias para info operando anterior y operación en memoria
# Falta por controlar el tamaño máximo de entrada para que no se salga de la pantalla.

from tkinter import *
from PIL import ImageTk, Image
import os

def botonNum(nuevaCifra):
    global resetPantalla

    if resetPantalla != False:
        if nuevaCifra==",":
            infoPantalla.set("0,")
        else:
            infoPantalla.set(nuevaCifra)
        infoPantallaResultado.set(formatoPantalla(resultadoOper))
        infoPantallaOper.set(tipoOper)
        resetPantalla=False
    else:
        if infoPantalla.get() == "0" and nuevaCifra == "0":
            pass
        elif infoPantalla.get() == "0" and nuevaCifra != "0" and nuevaCifra != ",":
            infoPantalla.set(nuevaCifra)
        elif nuevaCifra == ",":
            if infoPantalla.get() == "0":
                infoPantalla.set("0,")
            elif infoPantalla.get().count(",")>0:
                pass
            else:
                infoPantalla.set(infoPantalla.get() + nuevaCifra)
        else:
            infoPantalla.set(infoPantalla.get() + nuevaCifra)

def reiniciar():
    global resultadoOper
    global tipoOper
    infoPantalla.set("0")
    infoPantallaOper.set("")
    infoPantallaResultado.set("")
    resultadoOper=0
    tipoOper=""

def borrarUltima():
    if infoPantalla.get() == "0":
        pass
    else:
        infoPantalla.set(infoPantalla.get()[0:(len(infoPantalla.get())-1)])
        if infoPantalla.get() == "":
            infoPantalla.set("0")

def operacion(oper):
    global tipoOper
    global resultadoOper
    global resetPantalla
   
    if oper=="RESULTADO" and tipoOper=="":
        pass
    
    if tipoOper=="":
        resultadoOper = float(infoPantalla.get().replace(",", "."))
        resetPantalla=True
        tipoOper=oper
    else:
        operandoActual = float(infoPantalla.get().replace(",", "."))
        infoPantallaOper.set(oper)
        infoPantallaResultado.set("")
        if tipoOper == "SUMA":
            resultadoOper=resultadoOper + operandoActual
        elif tipoOper=="RESTA":
            resultadoOper=resultadoOper - operandoActual
        elif tipoOper=="MULT":
            resultadoOper=resultadoOper * operandoActual
        elif tipoOper=="DIV":
            try:
                resultadoOper = resultadoOper / operandoActual
            except ZeroDivisionError:
                resultadoOper = 0
        
        infoPantalla.set(formatoPantalla(resultadoOper))
        if oper=="RESULTADO":
            tipoOper=""
            infoPantallaOper.set(tipoOper)
            infoPantallaResultado.set("")
        else:
            tipoOper = oper
            resetPantalla=True

def formatoPantalla(num):
    if num % 1 == 0:
        return str(int(num))
    else:
        numTemp=str(num)
        return numTemp.replace(".", ",")
    

# --- Variables para la gestión de resultado y operación ---
tipoOper=""
resultadoOper=0
resetPantalla=False

# --- Montamos raíz y frame principal ---
root=Tk()
root.title("PyCalc")

try:
    root.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open(os.path.dirname(__file__)+'/py_calc.ico')))
except:
    pass

frame0=Frame(root,bg="grey")
frame0.pack()

# --- Pantalla ---
infoPantalla=StringVar()
pantalla=Entry(frame0,font=("Arial 12"),textvariable=infoPantalla)
pantalla.grid(row="1", column="1", padx="5", pady="5",ipadx="10", ipady="10", columnspan=4)
pantalla.config(width=27,fg="#03f943",justify="right", state="readonly",readonlybackground="black")
infoPantalla.set("0")

# --- Pantallas secundarias ---
infoPantallaResultado=StringVar()
pantallaResultado=Entry(frame0,textvariable=infoPantallaResultado)
pantallaResultado.grid(row="2", column="1",padx="2",pady="2",columnspan=3)
pantallaResultado.config(width=33,fg="black", justify="right",state="readonly", readonlybackground="lightgrey")
infoPantallaResultado.set("")

infoPantallaOper = StringVar()
pantallaOper=Entry(frame0,textvariable=infoPantallaOper)
pantallaOper.grid(row="2", column="4", padx="2", pady="2", columnspan=1)
pantallaOper.config(width=8,fg="black", justify="center", state="readonly",readonlybackground="lightgrey")
infoPantallaOper.set("")


# --- Fila botones 1 ---
botonInicio=Button(frame0,text="CE",width=18,height=2,command=reiniciar)
botonInicio.grid(row="3",column="1",columnspan=2)
botonBorrar = Button(frame0, text="<==", width=18,height=2, command=borrarUltima)
botonBorrar.grid(row="3",column="3",columnspan=2)


# --- Fila botones 2 ---
boton7=Button(frame0,text="7",width=8,height=2,command=lambda:botonNum("7"))
boton7.grid(row="4",column="1")
boton8=Button(frame0,text="8",width=8,height=2,command=lambda:botonNum("8"))
boton8.grid(row="4",column="2")
boton9=Button(frame0,text="9",width=8,height=2,command=lambda:botonNum("9"))
boton9.grid(row="4",column="3")
botonDiv = Button(frame0, text="/", width=8, height=2,command=lambda: operacion("DIV"))
botonDiv.grid(row="4",column="4")

# --- Fila botones 3 ---
boton4=Button(frame0,text="4",width=8,height=2,command=lambda:botonNum("4"))
boton4.grid(row="5",column="1")
boton5=Button(frame0,text="5",width=8,height=2,command=lambda:botonNum("5"))
boton5.grid(row="5",column="2")
boton6=Button(frame0,text="6",width=8,height=2,command=lambda:botonNum("6"))
boton6.grid(row="5",column="3")
botonMult = Button(frame0, text="*", width=8, height=2,command=lambda: operacion("MULT"))
botonMult.grid(row="5",column="4")

# --- Fila botones 4 ---
boton1=Button(frame0,text="1",width=8,height=2,command=lambda:botonNum("1"))
boton1.grid(row="6",column="1")
boton2=Button(frame0,text="2",width=8,height=2,command=lambda:botonNum("2"))
boton2.grid(row="6",column="2")
boton3=Button(frame0,text="3",width=8,height=2,command=lambda:botonNum("3"))
boton3.grid(row="6",column="3")
botonResta = Button(frame0, text="-", width=8, height=2,command=lambda: operacion("RESTA"))
botonResta.grid(row="6",column="4")

# --- Fila botones 5 ---
boton0=Button(frame0,text="0",width=8,height=2,command=lambda:botonNum("0"))
boton0.grid(row="7",column="1")
botonComa=Button(frame0,text=",",width=8,height=2,command=lambda:botonNum(","))
botonComa.grid(row="7",column="2")
botonIgual=Button(frame0,text="=",width=8,height=2,command=lambda:operacion("RESULTADO"))
botonIgual.grid(row="7",column="3")
botonSuma=Button(frame0,text="+",width=8,height=2,command=lambda:operacion("SUMA"))
botonSuma.grid(row="7",column="4")

# --- Bucle ejecuión ventana ---
root.mainloop()
