""" Este es el lugar adecuado para documentar un módulo, la primera línea """

"""
Para paquetes, los comentarios se informan en la primera línea del
__init__.py

"""

class Operaciones:

    """ Este es el lugar adecuada para documentar una clase, la primera línea
        En este caso, esta clase de ejemplo agrupa operaciones matemáticas sencillas.
    """

    def sumar(op1, op2):
        """ Este es el lugar apropiado para documentar una función, la primera línea
            Operación de suma con dos factores.
        """

        print("El resultado de la suma es: ", str(op1+op2))


    def restar(op1, op2):
        """ Este es el lugar apropiado para documentar una función, la primera línea
            Operación de resta.
        """

        print("El resultado de la resta es: ", str(op1-op2))


    def multiplicar(op1, op2):
        """ Este es el lugar apropiado para documentar una función, la primera línea
            Operación de multiplicación con dos factores.
        """

        print("El resultado de la multiplicación es: ", str(op1*op2))


    def dividir(op1, op2):
        """ Este es el lugar apropiado para documentar una función, la primera línea
            Oreración de división.
        """
        
        if op2 == 0:
            print("No se puede dividir por cero.")
        else:
            print("El resultado de la division es: ", str(op1/op2))


def potencia(base,exponente):

    """ 
        Comentarios de la función
        Esta función calcula e imprime en consola la potencia de los argumentos de entrada.
    """
    print("El resultado de la potencia es: ", str(pow(base,exponente)))



print(potencia.__doc__) #Imprime los comentarios de una función
help(potencia) # Imprime los comentarios y ayuda genérica de una función

help(Operaciones) # Imprime por consola la ayuda de una clase con todas sus funciones
print(Operaciones.restar.__doc__)  # Imprime los comentarios de una función de clase
help(Operaciones.restar) # Imprime los comentarios y ayuda genérica de una función de clase
print(dir(Operaciones)) # Imprime un listado de las variables y funciones

# Modificar directorio al del fichero actual
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import Modulo_documentado
help(Modulo_documentado) # Imprime información completa y comentarios sobre un módulo importado

