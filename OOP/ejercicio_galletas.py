class Galleta():

    def __init__(self, sabor, color): #Método constructor
        self.sabor = sabor
        self.color = color
        self.chocolate = False
        print(f"Se acaba de crear una galleta {self.color} y {self.sabor}.")

    def __del__(self): #Método destructor
        print(f"La galleta {self} se está borrando de la memoria")

    def saludar(self):
        print("Hola, soy una galletita.")
        print(self)

    def chocolatear(self):
        self.chocolate=True


galleta1=Galleta("dulce","marrón clarito")

#Galleta.chocolate=True
""" Si se modifica una atributo de clase en tiempo de ejecución,
los objetos ya instanciados se verán modificados """

galleta2=Galleta("coco","blanca")
print(galleta1.chocolate)
print(galleta2.chocolate)

galleta1.saludar()
galleta1.chocolatear()
print(galleta1.chocolate)

#galleta1.__del__()
#galleta2.__del__()
del(galleta2)
del(galleta1)


print("Fin del horneado")
