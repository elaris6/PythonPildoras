"""
El módulo unittest, a veces referido como PyUnit, forma parte de una serie de frameworks
conocidos como xUnit. Estas librerías se encuentran en la mayoría de lenguajes y son casi
un estándard a la hora de programar pruebas unitarias.

A diferencia de doctest, unittest ofrece la posibilidad de crear las pruebas en el propio 
código implementando una clase llamada unittest.TestCase en la que se incluirá un kit o 
batería de pruebas. Cada una de las pruebas puede devolver tres respuestas en función del 
resultado:

    OK: Para indicar que la prueba se ha pasado éxitosamente.
    FAIL: Para indicar que la prueba no ha pasado éxitosamente lanzaremos una excepción AssertionError (sentencia verdadero-falso)
    ERROR: Para indicar que la prueba no ha pasado éxitosamente, pero el resultado en lugar de ser una aserción es otro error.

Doc oficial: https://docs.python.org/3/library/unittest.html

"""

import unittest

def doblar(a): return a*2
def sumar(a, b): return a+b
def es_par(a): return 1 if a % 2 == 0 else 0


class PruebasFunciones(unittest.TestCase):

    def test_doblar(self):
        self.assertEqual(doblar(10), 20)
        self.assertEqual(doblar('Ab'), 'AbAb')

    def test_sumar(self):
        self.assertEqual(sumar(-15, 15), 0)
        self.assertEqual(sumar('Ab', 'cd'), 'Abcd')

    def test_es_par(self):
        self.assertEqual(es_par(11), False)
        self.assertEqual(es_par(68), True)

class PruebasMetodosCadenas(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hola'.upper(), 'HOLA')

    def test_isupper(self):
        self.assertTrue('HOLA'.isupper())
        self.assertFalse('Hola'.isupper())

    def test_split(self):
        s = 'Hola mundo'
        self.assertEqual(s.split(), ['Hola', 'mundo'])

"""
Preparación y limpieza de pruebas.
TestCase incorpora dos métodos extras. El primero es setUp() y sirve para preparar el 
contexto de las pruebas, por ejemplo para escribir unos valores de prueba en un fichero 
conectarse a un servidor o a una base de datos.

Luego tendríamos tearDown() para hacer lo propio con la limpieza, borrar el fichero, 
desconectarse del servidor o borrar las entradas de prueba de la base de datos.

Este proceso de preparar el contexto se conoce como test fixture o accesorios de prueba.
"""

class PruebaTestFixture(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto")
        self.numeros = [1, 2, 3, 4, 5]

    def test(self):
        print("Realizando una prueba")
        r = [doblar(n) for n in self.numeros]
        self.assertEqual(r, [2, 4, 6, 8, 10])

    def tearDown(self):
        print("Destruyendo el contexto")
        del(self.numeros)

if __name__ == "__main__":
    unittest.main()
