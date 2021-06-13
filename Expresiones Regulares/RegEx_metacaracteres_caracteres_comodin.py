""" Anclas y Clases de caracteres """

import re

lista_nombres = ['Israel Balboa','Jorge Salas','Diego Muriel','Daniel Peña','Carlos Gonzalez','Joaquín García']

# Usamos el acento circunflejo para buscar el inicio deseado
for elemento in lista_nombres:
    if re.findall('^D',elemento):
        print(elemento)

print("---")

# Usamos el dólar para buscar el final deseado en la cadena
for elemento in lista_nombres:
    if re.findall('a$', elemento):
        print(elemento)

print("---")

lista_palabras=['hombre','mujer','niños','perros','niñas','gatos']

# Usamos los corchetes para buscar coincidencias con unos caracteres concretos
for elemento in lista_palabras:
    if re.findall('niñ[oa]s', elemento):
        print(elemento)
