"""A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
Finalizar al ingresar el número 0, el cual no debe guardarse.
B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original 
que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, 
cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 
Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: 
[(5,3), (16,1), (2,2), (57,1)]"""

# A
def funcion_a():
    lista=[]
    while True:
        print('Introduce un nuevo elemento numérico para la lista (0 para salir): ')
        nuevo=int(input())
        if nuevo == 0:
            break
        else: 
            lista.append(nuevo)

    print(lista)

# B
def funcion_b():
    print('Inserta un número para eliminar de la lista: ')
    num_eliminar=int(input())
    if num_eliminar in lista:
        posicion=lista.index(num_eliminar)
        lista.pop(posicion)
    else:
        print ('El elemento no está en la lista.')

    print(lista)

# C
def funcion_c():
    suma_lista=0
    for i in range(len(lista)):
        suma_lista+=lista[i]

    print('La suma de los valores de la lista es: '+str(suma_lista))

# D
def funcion_d():
    print('Inserta un número para crear una nueva lista con valores menores que este: ')
    num_tope = int(input())
    nueva_lista=[]
    for i in range(len(lista)):
        if num_tope>lista[i]:
            nueva_lista.append(lista[i])

    print('Lista original: '+str(lista))
    print('Nueva lista: '+str(nueva_lista))

# E
def funcion_e():
    lista_1=[1,3,15,17,19,11,13,15,17,19,21]
    lista_2=[]

    for i in range(len(lista_1)):
        if (lista_1[i],lista_1.count(lista_1[i])) not in lista_2:
            print('No está, añado: ' + str((lista_1[i], lista_1.count(lista_1[i]))))
            lista_2.append((lista_1[i], lista_1.count(lista_1[i])))
        else:
            print('Si está en la lista. No añado: ' + str((lista_1[i], lista_1.count(lista_1[i]))))

    print(lista_2)

funcion_e()
