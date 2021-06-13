""" Crear un programa para gestionar datos de los socios de un club, permitiendo:

-Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar son: 
número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n).

El programa debe iniciar con los datos de los socios fundadores ya cargados:
Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.

-Informar cantidad de socios del club.
-Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
-Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.
-Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
-Imprimir el listado de socios completo. 
"""

import os
import time

socios={1: {"nombre": "Israel Balboa", "fecha_ingreso": "09/09/1985", "cuotas": False},
        2: {"nombre": "Jorge Salas", "fecha_ingreso": "09/09/1985", "cuotas": True},
        3: {"nombre": "Diego Muriel", "fecha_ingreso": "09/09/1985", "cuotas": True},
        }

# Función imprime menú y recoge opción
def menu():
    while True:
        print()
        print("Opciones del menú:")
        print("1. Imprimir listado socios.")
        print("2. Informar cantidad de socios.")
        print("3. Actualizar pagos socio.")
        print("4. Actualizar fechas de ingreso.")
        print("5. Baja socio.")
        print("6. Alta socio.")
        print("X. Salir.")
        print()
        opcion=input("Elija una opción del menú: ")
        if opcion not in ["1","2","3","4","5","6","x","X"]:
            print("Opción incorrecta. Por favor, elija una opción del menú.")
        else:
            break
    return opcion

# Opción menú 1
def imprime_socios():
    for num_socio in socios.keys():
        print("Datos socio: "+str(num_socio), end="\n   ")
        print("Nombre: "+socios[num_socio]["nombre"]+"\n   ",
              "Fecha ingreso: "+socios[num_socio]["fecha_ingreso"], sep="", end="\n   ")
        if socios[num_socio]["cuotas"] == True:
            print("Cuotas al día: Si")
        else:
            print("Cuotas al día: No")

# Opción menu 2
def cuenta_socios():
    print("El número de socios es: "+str(len(socios.keys())))
    print()

# Opción menú 3
def actualiza_pagos():
    num_socio=int(input("Introduce un número de socio para poner al día sus pagos: "))
    if socios.get(num_socio) == None:
        print("El número de socio introducido no existe.")
    else:
        socios[num_socio]["cuotas"] = True
    
# Opción menú 4
def actualiza_fecha_ingreso():
    print("Introduce la fecha incorrecta a buscar.")

    dia = int(input("Introduce el día: "))
    while True:
        if 0<dia<32:
            break
        else:
            dia=int(input("Valor incorrecto. Introduce día: "))
    if dia < 10:
        dia = "0"+ str(dia)
    else:
        dia = str(dia)
    
    mes = int(input("Introduce el mes: "))
    while True:
        if 0 < mes < 13:
            break
        else:
            mes = int(input("Valor incorrecto. Introduce mes: "))
    if mes < 10:
        mes = "0" + str(mes)
    else:
        mes = str(mes)

    anno = input("Introduce el año: ")
    while True:
        if 1978 < int(anno) < int(time.strftime("%Y")):
            break
        else:
            anno = input("Valor incorrecto. Introduce año: ")

    fecha_incorrecta=dia+"/"+mes+"/"+anno

    print("\nIntroduce la fecha correcta que se debe informar.")

    dia = int(input("Introduce el día: "))
    while True:
        if 0 < dia < 32:
            break
        else:
            dia = int(input("Valor incorrecto. Introduce día: "))
    if dia < 10:
        dia = "0" + str(dia)
    else:
        dia = str(dia)

    mes = int(input("Introduce el mes: "))
    while True:
        if 0 < mes < 13:
            break
        else:
            mes = int(input("Valor incorrecto. Introduce mes: "))
    if mes < 10:
        mes = "0" + str(mes)
    else:
        mes = str(mes)

    anno = input("Introduce el año: ")
    while True:
        if 1978 < int(anno) < int(time.strftime("%Y")):
            break
        else:
            anno = input("Valor incorrecto. Introduce año: ")

    fecha_correcta = dia+"/"+mes+"/"+anno

    actualizaFecha=0
    for socio in socios:
        if socios.get(socio)["fecha_ingreso"]==fecha_incorrecta:
            socios.get(socio)["fecha_ingreso"]=fecha_correcta
            print("Actualizada fecha ingreso socio: "+str(socio))
            actualizaFecha=1
    if actualizaFecha==0:
        print("\nNingún socio hallado con la fecha de ingreso incorrecta indicada.")


# Opción menú 5
def baja_socio():
    socioBaja=input("Introduce el nombre y apellido del socio para darlo de baja: ")
    eliminar=[]
    for socio in socios:
        if socios.get(socio)["nombre"]==socioBaja:
            print("Datos socio a eliminar: "+str(socio), end="\n   ")
            print("Nombre: "+socios[socio]["nombre"]+"\n   ",
              "Fecha ingreso: "+socios[socio]["fecha_ingreso"], sep="", end="\n   ")
            if socios[socio]["cuotas"] == True:
                print("Cuotas al día: Si")
            else:
                print("Cuotas al día: No")
            eliminar.append(socio)
    for i in eliminar:
        socios.pop(i)
           
# Opción menú 6
def alta_socio():
    num_socio=1+max(socios.keys())
    nombre_socio=input("Introduce el nombre y apellido del socio: ")
    fecha_ingreso=input("Quieres asignar como fecha de ingreso la fecha de hoy? S/N: ")
    while True:
        if fecha_ingreso in ("S","N","s","n"):
            break
        else:
            fecha_ingreso = input(
                "Opción incorrecta.\nQuieres asignar como fecha de ingreso la fecha de hoy? S/N: ")
    if fecha_ingreso in ("S","s"):
        fecha_ingreso=time.strftime("%d/%m/%Y")
    else:
        print("Introduce la fecha de ingreso deseada.")

        dia = int(input("Introduce el día: "))
        while True:
            if 0 < dia < 32:
                break
            else:
                dia = int(input("Valor incorrecto. Introduce día: "))
        if dia < 10:
            dia = "0" + str(dia)
        else:
            dia = str(dia)
        mes = int(input("Introduce el mes: "))
        while True:
            if 0 < mes < 13:
                break
            else:
                mes = int(input("Valor incorrecto. Introduce mes: "))
        if mes < 10:
            mes = "0" + str(mes)
        else:
            mes = str(mes)
        anno = input("Introduce el año: ")
        while True:
            if 1978 < int(anno) < int(time.strftime("%Y")):
                break
            else:
                anno = input("Valor incorrecto. Introduce año: ")
        fecha_ingreso = dia+"/"+mes+"/"+anno

    try:
        socios.update({num_socio:{"nombre":nombre_socio,"fecha_ingreso":fecha_ingreso,"cuotas":True}})
    except:
        print("No ha sido posible insertar el nuevo socio. Ha ocurrido un error en el programa.")


# Bloque principal del programa
while True:
    opcion=menu()
    if opcion == 'x' or opcion == 'X':
        print("Fin del programa.")
        #time.sleep(2)
        #os.system("cls")
        break
    elif int(opcion) == 1:
        imprime_socios()
    elif int(opcion) == 2:
        cuenta_socios()
    elif int(opcion) == 3:
        actualiza_pagos()
    elif int(opcion) == 4:
        actualiza_fecha_ingreso()
    elif int(opcion) == 5:
        baja_socio()
    elif int(opcion) == 6:
        alta_socio()

# Fin bloque principal
