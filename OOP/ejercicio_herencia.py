#https://docs.hektorprofe.net/python/herencia-en-la-poo/ejercicios/

from random import shuffle, sample

class Vehiculo():

    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Color {self.color}, {self.ruedas} ruedas'


class Coche(Vehiculo):

    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + f', velocidad {self.velocidad}, {self.cilindrada} cc'

class Camioneta(Coche):

    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        Coche.__init__(self,color,ruedas,velocidad,cilindrada)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + f', {self.carga} kg de carga'

class Bicicleta(Vehiculo):

    def __init__(self,color,ruedas,tipo):
        Vehiculo.__init__(self,color,ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return Vehiculo.__str__(self) + f', tipo {self.tipo}'

class Motocicleta(Coche,Bicicleta):

    def __init__(self,color,ruedas,velocidad,cilindrada,tipo):
        Coche.__init__(self,color,ruedas,velocidad,cilindrada)
        Bicicleta.__init__(self,color,ruedas,tipo)

    def __str__(self):
        return Coche.__str__(self) + f', tipo {self.tipo}'


def catalogar(listaVehiculos, ruedas=None):

    if ruedas == None:
        for vehiculo in listaVehiculos:
            print(type(vehiculo).__name__ + ':',vehiculo)
    else:
        count=0
        listaCoincidentes=[]
        for vehiculo in listaVehiculos:
            if ruedas == vehiculo.ruedas:
                listaCoincidentes.append(vehiculo)
                count+=1
        if count == 0:
            print(f'Se han encontrado {count} vehículos con {ruedas} ruedas.')
        else:
            print(f'Se han encontrado {count} vehículos con {ruedas} ruedas:')
            for vehiculo in listaCoincidentes:
                print(type(vehiculo).__name__ + ':',vehiculo)


coche1 = Coche('azul',4,190,1800)
coche2 = Coche('plateado',4,210,2000)
furgo1 = Camioneta('blanca',4,165,2200,2000)
furgo2 = Camioneta('verde', 6, 170, 2800, 3500)
bici1 = Bicicleta('naranja',2,'deportiva')
bici2 = Bicicleta('azul', 2, 'urbana')
moto1 = Motocicleta('blanca',2,180,1000,'urbana')
moto2 = Motocicleta('negra', 2, 205, 600, 'deportiva')
moto2 = Motocicleta('amarilla', 3, 150, 1800, 'urbana')

listaVehiculos = [coche1, coche2, bici1, bici2, moto1, moto2, furgo1,furgo2]

shuffle(listaVehiculos)
numRuedas = sample([0,2,3,4,6],1)
print('\nListar filtrados:')
catalogar(listaVehiculos,numRuedas[0])
print('\nListar todos:')
catalogar(listaVehiculos)









