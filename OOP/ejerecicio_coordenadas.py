""" Ejercicio para practicar la OOP en base a coordenadas y vectores """

from math import sqrt

class Punto():

    """ Clase Punto que inicializa un objeto punto en base a sus coordenadas """
    # https://docs.hektorprofe.net/python/programacion-orientada-a-objetos/ejercicios/

    """ Forma más sencilla de asignar valores por defecto
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y"""

    def __init__(self,**kwargs):

        self.ejeX=0
        self.ejeY=0

        for kwarg in kwargs:
            if kwarg == 'ejeX':
                self.ejeX=kwargs[kwarg]
            if kwarg == 'ejeY':
                self.ejeY = kwargs[kwarg]

    def __str__(self):
        return f'({self.ejeX},{self.ejeY})'

    def cuadrante(self):
        if self.ejeX == 0 and self.ejeY == 0:
            return "Estoy en el centro."
        elif self.ejeX == 0:
            if self.ejeY > 0:
                return "Estoy sobr el eje Y en positivo."
            else:
                return "Estoy sobre el eje Y en negativo."
        elif self.ejeY == 0:
            if self.ejeX > 0:
                return "Estoy sobr el eje X en positivo."
            else:
                return "Estoy sobre el eje X en negativo."
        elif self.ejeY > 0:
            if self.ejeX > 0:
                return "Estoy en el cuadrante 1."
            else:
                return "Estoy en el cuadrante 2."
        else:
            if self.ejeX > 0:
                return "Estoy en el cuadrante 4."
            else:
                return "Estoy en el cuadrante 3."
    
    def vector(self,otroPunto):
        ejeXRes = otroPunto.ejeX - self.ejeX
        ejeYRes = otroPunto.ejeY - self.ejeY

        return f'({ejeXRes},{ejeYRes})'


    def distancia(self,otroPunto):
        ejeXRes = otroPunto.ejeX - self.ejeX
        ejeYRes = otroPunto.ejeY - self.ejeY
        distancia = sqrt((ejeXRes**2)+(ejeYRes**2))
        return distancia

class Rectangulo():
    #Clase que crea un rectángulo en base a dos puntos recibidos que definen la diagonal

    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1=punto1
        self.punto2=punto2

    def base(self):
        return abs(self.punto1.ejeX - self.punto2.ejeX)

    def altura(self):
        return abs(self.punto1.ejeY - self.punto2.ejeY)

    def area(self):
        return self.base() * self.altura()


def puntoMasLejano(listaPuntos):

    origen = Punto(ejeX=0, ejeY=0)
    listaPuntosLejanos = []
    maxDistancia = 0
    for punto in listaPuntos:
        if punto.distancia(origen) > maxDistancia:
            listaPuntosLejanos = []
            listaPuntosLejanos.append(punto)
            maxDistancia = punto.distancia(origen)
        elif punto.distancia(origen) == maxDistancia:
            listaPuntosLejanos.append(punto)
    return listaPuntosLejanos

""" PRUEBAS """

punto1=Punto(ejeX=2,ejeY=3)
punto2=Punto(ejeX=5,ejeY=5)
punto3=Punto(ejeX=-3,ejeY=-1)
punto4=Punto(ejeX=0,ejeY=0)
punto5=Punto(ejeX=-5, ejeY=-5)

print(punto1, punto1.cuadrante())
print(punto2, punto2.cuadrante())
print(punto3, punto3.cuadrante())
print(punto4, punto4.cuadrante())
print(f'El vector entre {punto1} y {punto2} es {punto1.vector(punto2)}')
print(f'El vector entre {punto2} y {punto1} es {punto2.vector(punto1)}')
print(f'La distancia entre {punto1} y {punto4} es {punto1.distancia(punto4)}')
print(f'La distancia entre {punto2} y {punto4} es {punto2.distancia(punto4)}')
print(f'La distancia entre {punto3} y {punto4} es {punto3.distancia(punto4)}')

listaPuntos = [punto1, punto2, punto3, punto4, punto5]

print('\nEl punto o puntos más alejados del origen son: ')
for punto in puntoMasLejano(listaPuntos):
    print(punto)

print('\nRectángulo')
rectangulo = Rectangulo(punto1,punto2)
print(f'La base del rectángulo es {rectangulo.base()}\nLa altura del rectángulo es {rectangulo.altura()}\nEl área del rectángulo es {rectangulo.area()}')
