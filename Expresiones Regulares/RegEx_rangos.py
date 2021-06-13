import re

lista = ['MA1','BA.1','SE1','MA2','MA3','BA.2','SE2','MA4','BA3','SE3','MAA','BA:A','MAB','MA5','MAC']

for elemento in lista:
    if re.findall('MA[0-3]',elemento): # Rango de caracteres incluidos los extremos
        print(elemento)
print('--------------------------')
for elemento in lista:
    if re.findall('MA[^0-3]', elemento):  # Rango negado (opuesto) de caracteres incluidos los extremos
        print(elemento)
print('--------------------------')
for elemento in lista:
    if re.findall('MA[0-3A-B]', elemento): #Dos rangos unidos para la misma posición
        print(elemento)
print('--------------------------')
for elemento in lista:
    if re.findall('BA[.:]', elemento):  # Caracteres no alfabéticos
        print(elemento)

