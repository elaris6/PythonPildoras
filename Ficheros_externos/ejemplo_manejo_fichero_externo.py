from io import open
# Creación y escritura de texto en un fichero
"""
archivo_texto=open(".\\archivo_ejemplo.txt","w")

texto="Una frase de ejemplo.\nOtra frase de ejemplo."

archivo_texto.write(texto)

archivo_texto.close()
"""

# Apertura en modo lectura y lectura fichero completo
"""
archivo_texto=open(".\\archivo_ejemplo.txt","r")

texto=archivo_texto.read()

archivo_texto.close()

print(texto)
"""

# Apertura en modo lectura y lectura por líneas
"""
archivo_texto=open(".\\archivo_ejemplo.txt","r")

lineas_texto=archivo_texto.readlines() #también existe lectura de una sóla línea con readline()

archivo_texto.close()

print(lineas_texto)

print(lineas_texto[1])

for linea in lineas_texto:
    print(linea)
"""

archivo_texto=open(".\\archivo_ejemplo.txt","a")

archivo_texto.write("\nTercera frase de ejemplo.")

archivo_texto.close()
