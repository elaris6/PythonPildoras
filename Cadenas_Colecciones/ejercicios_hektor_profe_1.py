#https://docs.hektorprofe.net/python/metodos-de-las-colecciones/ejercicios/

#EJERCICIO 1

cadena = 'un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro'

texto = "un día que el viento soplaba con fuerza#" \
        "mira como se mueve aquella banderola -dijo un monje#" \
        "lo que se mueve es el viento -respondió otro monje#" \
        "ni las banderolas ni el viento, " \
        "lo que se mueve son vuestras mentes -dijo el maestro"

"""
Objetivo:
Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
"""

print(cadena)
frases = cadena.split('#')
for i in range(len(frases)):
    frases[i]=frases[i].capitalize()
    if i == 0:
        frases[i]=frases[i]+'...'
    else:
        frases[i] = '- '+frases[i]+'.'
    print(frases[i])


#EJERCICIO 2

from random import randint

lista_numeros=[]
for i in range(20):
    lista_numeros.append(randint(0,20))

#print(lista_numeros)

def modificar(lista_numeros):

    #Creamos una copia de la lista, para no modificarla
    lista_trabajo = lista_numeros.copy()

    #Elimina elementos duplicados. Lo hacemos simplemente convirtiendo la lista en conjunto
    lista_trabajo=list(set(lista_trabajo))

    #Ordena de mayor a menor la lista
    lista_trabajo.sort(reverse=True)

    #Elimina todos los impares
    lista_temp=[]
    for num in lista_trabajo:
        if num%2 == 0:
            lista_temp.append(num)

    #Realiza la suma de los elementos restantes
    suma=sum(lista_temp)

    #Añadir la suma como primer elemento de la lista_numeros
    lista_temp.insert(0,suma)

    #Devolver la lista modificada
    return lista_temp

#Comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista
nueva_lista = modificar(lista_numeros)
print(lista_numeros)
print(nueva_lista)
print(nueva_lista[0] == sum(nueva_lista[1:]))
