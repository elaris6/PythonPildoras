""" FUCNIONES MAP"""
""" Aplica función a un elemento iterable """


class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} trabaja como {self.cargo} y su salario es {self.salario} €"


listaEmpleados = [
    Empleado("Juan", "Director", 5700),
    Empleado("Pepa", "Director", 6100),
    Empleado("Ana", "Adminsitrativo", 2700),
    Empleado("Jose", "Administrativo", 2500),
    Empleado("Mario", "Secretario", 1900),
]


def calculo_comision(empleado):
    if empleado.salario < 3000:
        empleado.salario=empleado.salario*1.07
    return empleado



listaSalidaMap = map(lambda e: Empleado(e.nombre,e.cargo,e.salario*1.07) if e.salario < 3000 else e , listaEmpleados)

for empleado in listaSalidaMap:
    print(empleado)
