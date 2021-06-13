# Script para leer un fichero línea a línea de varias maneras distintas

# Cargando todas las líneas en memoria read() - NO RECOMENDADDO -

"""
f = open("archivo.txt", "r")
contenido = f.read()
f.close()
"""

# Cargando todas las líneas en memoria readlines() - NO RECOMENDADDO PARA FICHEROS GRANDES -

"""
f = open("archivo.txt", "r")
lineas = f.readlines()
f.close()
"""

# Cargando las líneas una por una readline()

"""
f = open(".\contratos.txt", "r")
while(True):
    linea = f.readline()
    print(linea)
    if not linea:
        break
f.close()
"""

# Utilizando la iteración propia de Python


f = open("fichero.txt", "r")
for linea in f:
    print(linea)
f.close()

# Usando la sentencia with que cierra el fichero de forma automática al terminar su bloque de ejecución
with open("fichero.txt", "r") as fichero:
    for linea in fichero:
        print(linea)

