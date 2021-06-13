""" FUNCION FILTER """
""" Filtra una lista de elemenos devolviendo solo los que cumplan una condición """

def numero_par(num):
    if num % 2 == 0:
        return True

numeros = [31,24,56,79,13,19,20,84,45,66]

# Filter con lambda en lugar de función ordinaria
print(list(filter(lambda numero_par:numero_par%2==0, numeros)))

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    
    def __str__(self):
        return f"{self.nombre} trabaja como {self.cargo} y su salario es {self.salario} €"

listaEmpleados = [
    Empleado("Juan", "Director", 67000),
    Empleado("Pepa", "Director", 71000),
    Empleado("Ana", "Adminsitrativo", 37000),
    Empleado("Jose", "Administrativo", 35000),
    Empleado("Mario", "Secretario", 29000),
]

# Función para filtrar una lista de objetos
salarios_altos = filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado in salarios_altos:
    print(empleado)

