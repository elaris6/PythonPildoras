"""Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas.
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
-Agregar pasajeros a la lista de viajeros.
-Agregar ciudades a la lista de ciudades.
-Dado el DNI de un pasajero, ver a qué ciudad viaja.
-Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
-Dado el DNI de un pasajero, ver a qué país viaja. (redundante)
-Dado un país, mostrar cuántos pasajeros viajan a ese país.
-Salir del programa."""

# Función para buscar una ciudad en una lista de elementos (ciudad,país). Si pais = 1, devuelve el país correspondiente
def check_ciudad(ciudad,lista_ciudades,pais):
    encontrada = False
    for busqueda in lista_ciudades:
        if busqueda[0] == ciudad:
            encontrada = True
            break
    if pais == 0:
        return encontrada
    else:
        return busqueda[1]

# Función para buscar un pais en una lista de elementos (ciudad,país). Si ciudad = 1, devuelve la diudad correspondiente
def check_pais(pais, lista_ciudades, ciudad):
    encontrada = False
    for busqueda in lista_ciudades:
        if busqueda[1] == pais:
            encontrada = True
            break
    if ciudad == 0:
        return encontrada
    else:
        return busqueda[0]

# -Agregar pasajeros a la lista de viajeros.
def agr_pasajero():
    nombre=input('Introduce el nombre del pasajero: ')
    id_pasajero=int(input('Introduce el id numérico del pasajero: '))
    ciudad = input('Introduce la ciudad destino del pasajero: ')
    while check_ciudad(ciudad,destinos,0) == False:
        ciudad=input('La ciudad no es elegible. Introduce una cuidad entre la lista de destinos:')
    pasajeros.append((nombre,id_pasajero,ciudad))
    print ('Se ha agregado el pasajero: '+ nombre+', '+str(id_pasajero)+', '+ciudad)
    print()

# -Agregar ciudades a la lista de ciudades.
def agr_destino():
    ciudad = input('Introduce la ciudad destino: ')
    while check_ciudad(ciudad,destinos,0) == True:
        ciudad = input('La ciudad ya existe como destino. Introduce una cuidad que no exista:')
    pais = input('Introduce el país de la ciudad destino: ')
    destinos.append((ciudad,pais))
    print('Se ha añadido el siguiente destino: '+ciudad+', '+pais)
    print()
    
# -Dado el DNI de un pasajero, ver a qué ciudad viaja.
def cons_destino_pasajero():
    id_pasajero=int(input('Introduce el id del pasajero a buscar: '))
    encontrado=False
    for busqueda in pasajeros:
        if busqueda[1]==id_pasajero:
            encontrado=True
            break
    if encontrado == False:
        print('No se ha encontrado al pasajero en la lista de pasajeros.')
        print()
    else:
        print('La ciudad destino es: '+busqueda[2])
        pais=check_ciudad(busqueda[2],destinos,1)
        print('El país destino es: '+pais)    
        print()

# -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
def cons_pasajeros_ciudad():
    ciudad=input('Introduce la ciudad a consultar: ')
    if check_ciudad(ciudad,destinos,0) == False:
        print('La ciudad introducida no está en la lista de destinos.')
        print()
    else:
        cuenta=0
        for busqueda in pasajeros:
            if busqueda[2]==ciudad:
                cuenta+=1
        print('El número de pasajeros que van a la ciudad es: '+str(cuenta))
        print()

# -Dado un país, mostrar cuántos pasajeros viajan a ese país.
def cons_pasajeros_pais():
    pais=input('Introduce el país a consultar: ')
    if check_pais(pais, destinos, 0) == False:
        print('El país introducido no está en la lista de destinos.')
        print()
    else:
        ciudad = check_pais(pais, destinos, 1)
        cuenta = 0
        for busqueda in pasajeros:
            if busqueda[2] == ciudad:
                cuenta += 1
        print('El número de pasajeros que van a ese país es: '+str(cuenta))
        print()

    
# BLOQUE PRINCIPAL DEL PROGRAMA

pasajeros = [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"),
             ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa"), ("Israel Balboa", 123456, "Liverpool")]

destinos = [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"),
            ("Lisboa", "Portugal"), ("Liverpool", "Inglaterra"), ("Madrid", "España")]


while True:
    print('Eliaj una opción del menú:')
    print('1. Agregar pasajero.')
    print('2. Agregar destino.')
    print('3. Consultar destino pasajero.')
    print('4. Consultar pasajeros con destino a una ciudad.')
    print('5. Consultar pasajeros con destino a un país.')
    print('x. Salir.')
    opcion=input()
    if opcion == 'x' or opcion == 'X':
        print('Gracias por usar nuestra aplicación.')
        break
    elif opcion == '1':
        agr_pasajero()
    elif opcion == '2':
        agr_destino()
    elif opcion == '3':
        cons_destino_pasajero()
    elif opcion == '4':
        cons_pasajeros_ciudad()
    elif opcion == '5':
        cons_pasajeros_pais()


