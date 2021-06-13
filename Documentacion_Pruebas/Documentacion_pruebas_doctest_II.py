""" Uso de expresiones complejas ya anidadas en doctest
    Posibilidad de contemplar errores
"""

from math import sqrt

def raizCuadrada(listaNumeros):

    """
        La función devuelve una lista con la raíz cuadrada de cada argumento de la lista de entrada.
    
    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]
    
    >>> lista=[]
    >>> for i in [4,9,16,-90]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error

    """

    return [sqrt(n) for n in listaNumeros]


def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos

    Pueden ser números:
    >>> suma(5,10)
    15
    >>> suma(-5,7)
    2

    Cadenas de texto:
    >>> suma('aa','bb')
    'aabb'

    O listas:
    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> suma(a,b)
    [1, 2, 3, 4, 5, 6]

    Sin embargo no podemos sumar elementos de tipos diferentes:
    >>> suma(10,"hola")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>> suma("hola",10)
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str

    """

    return a+b


import doctest
doctest.testmod()


