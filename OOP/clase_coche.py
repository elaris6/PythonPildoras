class Coche():

    #Esto es un constructor, que especifica el estado inicial de un objeto de clase
    def __init__(self): 
        self.largo=250
        self.ancho=150
        self.__peso=1150 #Encapsulamiento de un atributo o propiedad, para que no se pueda modificar desde fuera de la clase
        self.__ruedas=4 #Encapsulamiento de un atributo o propiedad, para que no se pueda modificar desde fuera de la clase
        self.__enMarcha=False #Encapsulamiento de un atributo o propiedad, para que no se pueda modificar desde fuera de la clase

    def arrancar(self,contacto):
        if contacto and self.__enMarcha == False:
            check=self.__selfcheck()
            if not check:
                print("Algo ha ido mal en el chequeo interno. No se puede arrancar.")
            else:    
                self.__enMarcha = True
                print("Brrruuuunnn!")
        elif contacto and self.__enMarcha == True:
            print("No se puede arrancar, ya está arrancado!")
        elif not contacto and self.__enMarcha == True:
            print("Contacto fuera, coche parado!")
        elif not contacto and self.__enMarcha == False:
            print("No se puede para el coche, ya está parado!")

    def estado(self):
        print("El largo del coche es ",self.largo)
        print("El peso del coche es ",self.__peso)
        print("Está el coche arrancado? ",self.__enMarcha)

    def __selfcheck(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="ok"

        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="ok":
            return True
        else:
            return False


print("--- Creación de una primera instancia, ejemplar u objeto de clase")
miCoche=Coche()
miCoche.estado()
miCoche.arrancar(True)
miCoche.estado()

print("--- Creación de una segunda instancia, ejemplar u objeto de clase")
miCoche2=Coche()
miCoche2.peso=2000
miCoche2.estado()
miCoche2.arrancar(False)
