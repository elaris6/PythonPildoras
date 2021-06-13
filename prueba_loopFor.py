""" Bucle for ordinario especificando valor de inicio y fin
para la variable de control """
for i in range(1,5):
    print('Hello '+str(i))

# Si no se especifica valor de inicio para la variable del bucle, esta toma valor cero
for i in range(5):
    print('Hola '+str(i))

# Para inidcar el incremento con un valor distinto a uno se añade el elemento de incremnto
# al final del rango
for i in range(1,20,3):
    print('Valor de i: '+str(i))

# Bucle for con decremento
for i in range(20,1,-3):
    print('Valor de i: '+str(i))


""" Por qué no se ejecuta? """ # No se ejecuta porque range es una función que en ese caso devuelve un subconjunto vacío
for i in range(1,20,-3):
    print('Valor de i: '+str(i))
