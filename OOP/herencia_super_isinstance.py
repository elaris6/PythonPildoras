class Persona():
    def __init__(self,nombre, edad, residencia):
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia

    def descripcion(self):
        print("Nombre: ",self.nombre," Edad: ",self.edad," Lugar residencia: ",self.residencia)

class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_emepleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_emepleado)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario," Antigüedad: ",self.antiguedad)


persona1=Persona("Anotnio",55,"España")
persona1.descripcion()

persona2=Empleado(1500,15,"Pepe",47,"Colombia")
persona2.descripcion()

print(isinstance(persona2,Empleado)) #Comprueba si un objeto pertenece a una clase
print(isinstance(persona2,Persona))
print(isinstance(persona1,Empleado))
