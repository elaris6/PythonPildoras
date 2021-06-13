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


class PruebasUno(unittest.TestCase):
    def test(self):
        pass

class PruebasDos(unittest.TestCase):
    def test(self):
        raise AssertionError()

class PruebasTres(unittest.TestCase):
    def test(self):
        1/0


if __name__ == "__main__":
    unittest.main()
