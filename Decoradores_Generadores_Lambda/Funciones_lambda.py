"""FUNCIONES LAMBDA. AKA: ONLINE, ON THE GO """
""" Funciones anónimas para simplificar el código en caso de requerir cálculos sencillos """

# Función ordinaria sencilla
"""def area_triangulo(base,altura):
    return (base*altura)/2

def area_circulo(radio):
    return 3.1416*(radio**2)

def revertir(cadena):
    return cadena[::-1]
"""
# Función lambda equivalente
area_triangulo = lambda base,altura:(base*altura)/2
area_circulo = lambda radio:3.1416*(radio**2)
revertir = lambda cadena: cadena[::-1]

triangulo = area_triangulo(5, 7)
circulo = area_circulo(2.45)
vuelta = revertir('Hola')

print(triangulo,'\n', circulo,'\n', vuelta)

"""
Se pueden usar cláusulas del tipo IF ELSE y anidarlas dentro de una función lambda

lambda <arguments> : <Return Value if condition is True> if <condition> else <Return Value if condition is False>

lambda <args> : <return Value> if <condition > ( <return value > if <condition> else <return value>)

"""

lista = ['Hola','Adios','Buenos días']
elem = 'saludos'

if elem.upper() in [elem_lista.upper() for elem_lista in lista]:
    print('Encontrada')
else:
    print('No encontrada')

