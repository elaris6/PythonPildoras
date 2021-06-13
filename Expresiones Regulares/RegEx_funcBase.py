""" Algunos ejemplos de funciones RE para búsqueda en cadenas """

import re

cadena="Vamos a trabajar con expresiones regulares en Python. Usamos Python porque mola."

resultado = re.search('Python', cadena)

print(resultado) # Objeto de tipo Match
print(resultado.start())  # Posición donde empieza la coincidencia
print(resultado.end())  # Posición donde termina la coincidencia
print(resultado.span()) # Tupla con posiciones donde empieza y termina la coincidencia
print(resultado.string)  # Cadena sobre la que se ha realizado la búsqueda

print(len(re.findall('Python',cadena)))
print(len(re.findall('expresiones|regulares', cadena))) # La tubería funciona como OR



