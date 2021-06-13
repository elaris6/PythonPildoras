# Opción 1: Importar el módulo completo, requiere nombrar el módulo

import funciones as func # El "as" es opcional para crear un pseudónimo

func.dividir(4,0)

# Opción 2: Importar algún objeto u objetos asilados

from funciones import sumar

sumar(3,6)

# Opción 3: Importar todas los objetos del módulo

from funciones import *

multiplicar(3,6)

""" Python busca los módulos de usuario importados en la misma ubicación de ejecución
o en las rutas indicadas en la variable de entorno PYTHONPATH (no creada por defecto) """