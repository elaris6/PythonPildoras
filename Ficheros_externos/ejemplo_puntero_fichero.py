archivo_texto=open(".\\archivo_ejemplo.txt","r+")

print(archivo_texto.read())

# El método seek posiciona el puntero en un caracter concreto
archivo_texto.seek(5)

# El método read lee el número de caracteres pasados por parámetro
# desde la posición actual del puntero.
# Si no se le indica posicion, leerá hasta el final del fichero.
print(archivo_texto.read(9))

archivo_texto.close()

