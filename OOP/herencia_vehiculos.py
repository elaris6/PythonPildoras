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
        self.autonomia=100 #Tal como está la creación de la subclase BicicletaElectrica, la ejemplarización de clase daría error si pasamos marca y modelo.

    def recargar(self):
        self.cargando=True

class BicicletaElectrica(VElectricos,Vehiculos): #En la herencia múltiple se da preferencia en cuanto a constructores (o si tienen métodos con el mismo nombre) a la primera clase indicada que lo tenga (no tiene porque ser la primera)
    pass

miMoto=Moto("Honda","Rebel")
miMoto.caballito()
miMoto.estado()

miFurgo=Furgoneta("Ford","Transit")
miFurgo.arrancar()
miFurgo.estado()
print(miFurgo.carga(True))

miBici=BicicletaElectrica()
miBici.estado()