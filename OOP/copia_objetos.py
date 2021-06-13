""" COPIA DE OBJETOS """

from copy import copy

class Test:
    pass

test1 = Test()
test2 = test1 # Esto crea una referencia que apunta al mismo objeto, no crea un objeto nuevo
test3 = copy(test1)  # Esto realmente crea un objeto nuevo igual que el copiado

test1.algo = "Prueba"

print(test2 == test1)  # ¿Son el mismo objeto?
print(test1 == test3)  # ¿Son el mismo objeto?

try:
    print(test2.algo)
except Exception as e:
    print(e)

try:
    print(test3.algo)
except Exception as e:
    print(e)

# La función copy se puede utilizar también para copiar colecciones:

lista1 = [1, 2, 3]
lista2 = copy(lista1)
lista1 = None

print(lista1)
print(lista2)
