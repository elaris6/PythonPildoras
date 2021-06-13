# Función tradicional que devuelve una lista de pares
"""def generaPares1(limite):
    num=1
    listaNum=[]
    while num<limite:
        listaNum.append(num*2)
        num+=1
    return listaNum

print(generaPares1(10))
"""

# Función similar elaborada con un generador que va devolviendo los resultados y
# luego se queda en suspensión hasta la siguiente invocación.
def generaPares(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1

devuelvePares=generaPares(5)

#Controlando la excepción de fin del generador
for i in range(100):
    try:
        print(next(devuelvePares))
        print("El flujo avanza...{}".format(i+1))
    except StopIteration:
        print("Se acabó el rango del generador en la iteración {}".format(i+1))
        break

#La instrucción next() no se puede usar sobre colecciones normales
#Para ello, debemos convertirlas en objetos iterables con la función iter()

lista = [1, 2, 3, 4, 5]
lista_iterable = iter(lista)
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))

cadena = "Hola"
cadena_iterable = iter(cadena)
print(next(cadena_iterable))
print(next(cadena_iterable))
print(next(cadena_iterable))
print(next(cadena_iterable))



