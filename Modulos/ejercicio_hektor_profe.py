#https://docs.hektorprofe.net/python/modulos-y-paquetes/ejercicios/
#Ejercicio 3

import random
import math

def leer_numero(ini,fin,mensaje):
    while True:
        try:
            num=int(input(mensaje))
            if ini <= num <= fin:
                return num
            else:
                print("Número fuera de rango solicitado.")
        except ValueError:
            print("Valor introducido incorrecto.")

def generador():
    numeros=leer_numero(1,20,'¿Cuántos números quieres generar? [1-20]: ')
    modo=leer_numero(1,3,'¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ')
    numeros_aleatorios=[]
    for i in range(numeros):
        num = random.uniform(0, 100)
        print(f'Número {i} sin redondear: {num}')
        if modo == 1:
            num=math.ceil(num)
        elif modo == 2:
            num=math.floor(num)
        else:
            num=round(num)
        print(f'Número {i} redondeado: {num}')
        numeros_aleatorios.append(num)
    
    return numeros_aleatorios

generador()





