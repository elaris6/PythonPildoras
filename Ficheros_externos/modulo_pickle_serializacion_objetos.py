import pickle

class Vehiculos(): #Calse padre o superclase

    def __init__ (self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False

    def arrancar (self):
        self.enMarcha=True

    def acelerar (self):
        self.acelera=True

    def frenar (self):
        self.frena=True

    def estado (self):
        print("--- Info Vehículo ---")
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.enMarcha,"\nAcelera: ",self.acelera,"\nFrena: ",self.frena)

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgo está cargada"
        else:
            return "La furgo no está cargada"

class Moto(Vehiculos): #La clase Moto (subclase), hereda de la clase Vehículo (padre o superclase)
    hcaballito=False
    def caballito(self):
        self.hcaballito=True
    def estado (self): #Al crear un método con el mismo nombre que el de la clase padre se sobreescribe y anula al de la clase padre
        print("--- Info Vehículo ---")
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.enMarcha,"\nAcelera: ",self.acelera,"\nFrena: ",self.frena,"\nCaballito: ",self.hcaballito)

class VElectricos():
    def __init__ (self): 
        self.autonomia=100

    def recargar(self):
        self.cargando=True

class BicicletaElectrica(VElectricos,Vehiculos): #En la herencia múltiple se da preferencia en cuanto a constructores (o si tienen métodos con el mismo nombre) a la primera clase indicada que lo tenga (no tiene porque ser la primera)
    def __init__(self,marca,modelo):
        Vehiculos.__init__(self,marca,modelo)

# Creación objetos serializados en fichero
"""
coche1=Vehiculos("Ford","Mondeo")
furgo1=Furgoneta("Ford","Transit")
moto1=Moto("Honda","Rebel")

lista_vehiculos=[coche1,furgo1,moto1]

fichero=open("vehiculos","wb")

pickle.dump(lista_vehiculos,fichero)

fichero.close()

del(fichero)
"""

# Recuperación objetos serializados en fichero
# No serán usables si no contamos con las clases requeridas para manejar esos objetos

fichero_apertura=open("vehiculos","rb")

lectura_vehiculos=pickle.load(fichero_apertura)

fichero_apertura.close()

for v in lectura_vehiculos:
    print(v.estado())

