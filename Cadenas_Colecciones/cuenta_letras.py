""" Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. 
Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. 
Ejemplo: "r":5, "%":3, "a":8, "9":1.
¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, incluyendo el valor 0 para las letras que no
 aparecieron?
"""

# Función para inserta un nuevo string en una cadena de strings
def nuevo_string(lista_strings):
    string=input("Introduce un nuevo string: ")
    lista_strings.append(string)
    return lista_strings


# Bloque principal del programa
lista_strings=[]
for i in range(5):
    nuevo_string(lista_strings)

# Cuenta la ocurrencia de cada tipo de caracter
registro_caracteres={}
for string in lista_strings:
    for char in string:
        if char in registro_caracteres.keys():
            registro_caracteres[char]+=1
        else:
            registro_caracteres.setdefault(char,1)

print(registro_caracteres)

# Cuenta la ocurrencia solo de los caracteres tipo letra
registro_letras={}
alfabeto="abcdefghijklmnñopqrstuvwxyz"
for letra in alfabeto+alfabeto.upper():
    registro_letras[letra]=0
for clave in registro_caracteres.keys():
    if str(clave.lower()) in alfabeto:
        registro_letras[clave]=registro_caracteres[clave]
    
print(registro_letras)



