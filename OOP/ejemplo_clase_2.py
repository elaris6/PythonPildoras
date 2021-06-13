class coche():
    def __init__ (self): #creación de un constructor
        self.__largoChasis = 250  # encapsulamiento para proteger ese atributo
        self.__anchoChasis = 120  # encapsulamiento para proteger ese atributo
        self.__ruedas = 4  # encapsulamiento para proteger ese atributo
        self.__enMarcha = False  # encapsulamiento para proteger ese atributo

    def arrancar(self,arrancamos):
        self.__enMarcha=arrancamos
        if self.__enMarcha:
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene un largo de ", self.__largoChasis, " cm.")
        print("El coche tiene un ancho de", self.__anchoChasis, " cm.")
        print("El coche tiene ", self.__ruedas, " ruedas.")


cocheUno=coche() #instanciar, ejemplarizar una clase
print(cocheUno.arrancar(True))
print(cocheUno.estado())

cocheDos=coche()
print(cocheDos.arrancar(False))
cocheDos.__ruedas=6 #no se permite modificar un atributo encapsulado. No da error
print(cocheDos.estado())
