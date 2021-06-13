class coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False

    def arrancar(self,arrancamos):
        self.enMarcha=arrancamos
        if self.enMarcha:
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene un largo de ", self.largoChasis, " cm.")
        print("El coche tiene un ancho de", self.anchoChasis, " cm.")
        print("El coche tiene ", self.ruedas, " ruedas.")


cocheUno=coche() #instanciar, ejemplarizar una clase

print(cocheUno.arrancar(True))
print(cocheUno.estado())

cocheDos=coche()

print(cocheDos.arrancar(False))
cocheDos.ruedas=6
print(cocheDos.estado())
