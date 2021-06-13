#https://docs.hektorprofe.net/python/manejo-de-ficheros/ejercicios/
# ejercicio 2
def inicializar():
    fichero = open('contador.txt', 'w')
    fichero.write('0')
    fichero.close()
    return 0

def contador(accion=None):

    try:
        fichero=open('contador.txt','r')
        try:
            cont = fichero.read()
            print("Contador recién leído: ", cont)
            fichero.close()
            cont = int(cont)
        except:
            print('Error: Fichero corrupto.')
            inicializar()
            return 0
    except:
        cont=inicializar()

    print("Contador inicial: ", cont)

    fichero = open('contador.txt', 'r+')
    fichero.seek(0)
    if accion == 'inc':
        cont += 1
        fichero.write(str(cont))
        fichero.truncate()  # Importante para que no queden otros caracteres escritos si escribimos menos de la logintud que había
    elif accion == 'dec':
        if cont <= 0:
            print('No se puede decrementar el contador, ya tiene valor 0.')
        else:
            cont -= 1
            fichero.write(str(cont))
            fichero.truncate() #Importante para que no queden otros caracteres escritos si escribimos menos de la logintud que había
    
    print("Contador final: ", cont)
    fichero.close()
    
contador()

fichero = open('contador.txt', 'r')
cont = fichero.read()
print("Contador fuera de función: ", cont)
fichero.close()

"""
# Ejercicio resuelto

from io import open
import sys

fichero = open("contador.txt", "a+") 
fichero.seek(0)
contenido = fichero.readline()

if len(contenido) == 0:
    contenido = "0"
    fichero.write(contenido)

fichero.close()

# Vamos a intentar transformar el texto a un número
try:
    contador = int(contenido)

    # En función de lo que el usuario quiera...
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1

    print(contador)

    # Finalmente volvemos a escribir los cambios en el fichero
    fichero = open("contador.txt", "w")
    fichero.write( str(contador) )
    fichero.close()

except:
    print("Error: Fichero corrupto.")
"""
