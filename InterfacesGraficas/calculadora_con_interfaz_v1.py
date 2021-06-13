# Calculadora con interfaz gráfica
# v1. Funcional pero no concatena operaciones

from tkinter import *
from PIL import ImageTk, Image
import os

def botonNum(nuevaCifra):

    for c in operandoMostrar.get():
        if c not in "0123456789,-":
            reiniciar()
            break

    if operandoMostrar.get() == "0" and nuevaCifra == "0":
        pass
    elif operandoMostrar.get() == "0" and nuevaCifra != "0" and nuevaCifra != ",":
        operandoMostrar.set(nuevaCifra)
    elif nuevaCifra == ",":
        if operandoMostrar.get() == "0":
            operandoMostrar.set("0,")
        elif operandoMostrar.get().count(",")>0:
            pass
        else:
            operandoMostrar.set(operandoMostrar.get() + nuevaCifra)
    else:
        operandoMostrar.set(operandoMostrar.get() + nuevaCifra)

def reiniciar():
    global tipoOper
    global resultadoOper
    resultadoOper=0
    operandoMostrar.set("0")
    tipoOper=""

def borrarUltima():
    if operandoMostrar.get() == "0":
        pass
    else:
        operandoMostrar.set(operandoMostrar.get()[0:(len(operandoMostrar.get())-1)])
        if operandoMostrar.get() == "":
            operandoMostrar.set("0")

def operacion(oper):
    global operando1
    global tipoOper
    operando1=operandoMostrar.get()
    if operando1 == "Zero division error":
        operando1="0"
    tipoOper=oper
    operandoMostrar.set("0")
    
def resultado():
    global operando1
    global tipoOper
    resultadoOper=0
    operando1=float(operando1.replace(",","."))
    operando2=float(operandoMostrar.get().replace(",","."))

    if tipoOper=="suma":
        resultadoOper=operando1 + operando2
    elif tipoOper=="resta":
        resultadoOper=operando1 - operando2
    elif tipoOper=="mult":
        resultadoOper=operando1 * operando2
    elif tipoOper=="div":
        if operando2 == 0:
            tipoOper = "div0"
        else:
            resultadoOper = operando1 / operando2

    if tipoOper=="div0":
        operandoMostrar.set("Zero division error")
    elif resultadoOper % 1 == 0:
        resultadoOper=int(resultadoOper)
        resultadoOper = str(resultadoOper)
        operandoMostrar.set(resultadoOper)
    else:
        resultadoOper=str(resultadoOper)
        resultadoOper.replace(".",",")
        operandoMostrar.set(resultadoOper)

    tipoOper=""

operando1=StringVar
tipoOper=""
resultadoOper=0

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
operandoMostrar=StringVar()
pantalla=Entry(frame0,font=("Arial 12"),textvariable=operandoMostrar)
pantalla.grid(row="1", column="1", padx="5", pady="5",ipadx="10", ipady="10", columnspan=4)
pantalla.config(fg="#03f943",justify="right", state="readonly",readonlybackground="black")
operandoMostrar.set("0")


# --- Fila botones 1 ---
botonInicio=Button(frame0,text="CE",width=14,height=2,command=reiniciar)
botonInicio.grid(row="2",column="1",columnspan=2)
botonBorrar = Button(frame0, text="<==", width=14,height=2, command=borrarUltima)
botonBorrar.grid(row="2",column="3",columnspan=2)


# --- Fila botones 2 ---
boton7=Button(frame0,text="7",width=6,height=2,command=lambda:botonNum("7"))
boton7.grid(row="3",column="1")
boton8=Button(frame0,text="8",width=6,height=2,command=lambda:botonNum("8"))
boton8.grid(row="3",column="2")
boton9=Button(frame0,text="9",width=6,height=2,command=lambda:botonNum("9"))
boton9.grid(row="3",column="3")
botonDiv=Button(frame0,text="/",width=6,height=2,command=lambda:operacion("div"))
botonDiv.grid(row="3",column="4")

# --- Fila botones 3 ---
boton4=Button(frame0,text="4",width=6,height=2,command=lambda:botonNum("4"))
boton4.grid(row="4",column="1")
boton5=Button(frame0,text="5",width=6,height=2,command=lambda:botonNum("5"))
boton5.grid(row="4",column="2")
boton6=Button(frame0,text="6",width=6,height=2,command=lambda:botonNum("6"))
boton6.grid(row="4",column="3")
botonMult=Button(frame0,text="*",width=6,height=2,command=lambda:operacion("mult"))
botonMult.grid(row="4",column="4")

# --- Fila botones 4 ---
boton1=Button(frame0,text="1",width=6,height=2,command=lambda:botonNum("1"))
boton1.grid(row="5",column="1")
boton2=Button(frame0,text="2",width=6,height=2,command=lambda:botonNum("2"))
boton2.grid(row="5",column="2")
boton3=Button(frame0,text="3",width=6,height=2,command=lambda:botonNum("3"))
boton3.grid(row="5",column="3")
botonResta=Button(frame0,text="-",width=6,height=2,command=lambda:operacion("resta"))
botonResta.grid(row="5",column="4")

# --- Fila botones 5 ---
boton0=Button(frame0,text="0",width=6,height=2,command=lambda:botonNum("0"))
boton0.grid(row="6",column="1")
botonComa=Button(frame0,text=",",width=6,height=2,command=lambda:botonNum(","))
botonComa.grid(row="6",column="2")
botonIgual=Button(frame0,text="=",width=6,height=2,command=resultado)
botonIgual.grid(row="6",column="3")
botonSuma=Button(frame0,text="+",width=6,height=2,command=lambda:operacion("suma"))
botonSuma.grid(row="6",column="4")

# --- Bucle ejecuión ventana ---
root.mainloop()
