import sys

if len(sys.argv) > 1:
    for arg in sys.argv:
        print(arg)

"""
sys.argv es una lista de los parámetros de invocación,
en la que sys.argv[0] es el nombre del propio script de python.

c:\CODE\Python\Curso_Python>python prueba_parametros_externos.py param1 param2 param3
prueba_parametros_externos.py
param1
param2
param3

"""

