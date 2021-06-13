"""
El polimorfismo es una propiedad de la herencia por la que
objetos de distintas subclases pueden responder a una misma acción

La polimorfia es implícita en Python, ya que todas las clases son
subclases de una superclase común llamada Object. 

"""


class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazazo utilizando seis ruedas")

miVehic1=Moto()
miVehic1.desplazamiento()

miVehic2=Coche()
miVehic2.desplazamiento()

miVehic3=Camion()
miVehic3.desplazamiento()

def desplazamientoVehic(vehiculo):
    vehiculo.desplazamiento()

miVehic4=Moto()
desplazamientoVehic(miVehic4)
