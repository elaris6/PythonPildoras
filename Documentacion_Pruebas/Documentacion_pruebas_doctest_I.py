""" Incluir pruebas de comprobación automática en los comentarios """

import doctest
import os

def areaTrianagulo(base,altura):
    """ Calucla el área de un triángulo con la base y altura dadas 

    >>> areaTrianagulo(3,6)
    'El área del triángulo es: 9.0'

    >>> areaTrianagulo(4,7)
    'El área del triángulo es: 14.0'
    
    """
    
    return ('El área del triángulo es: '+str((base*altura)/2))

def checkMail(email):
    """ Función sencilla de validación de formato de email.

    >>> checkMail('prueba@prueba.com')
    True

    >>> checkMail('prueba@prueba@.com')
    False

    >>> checkMail('prueba.prueba.com')
    False

    >>> checkMail('@pruebaprueba.com')
    False

    >>> checkMail('pruebaprueba.com@')
    False

    """

    arroba=email.count('@')

    if (arroba != 1 or email.rfind('@') == (len(email)-1) or email[0] == '@'):
        return False
    else:
        return True

# Para evitar que se ejecute este código del módulo al importarlo desde otro lugar:
if __name__ == "__main__":
    doctest.testmod()
    
    # Se puede ejecutar también desde la terminal (- v para verbose):
    # c:\>python script.py [-v] 
