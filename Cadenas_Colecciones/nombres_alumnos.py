""" Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, 
finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel 
secundario, finalizando al ingresar “x”.
- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>
- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
- Informar qué nombres de nivel primario no se repiten en los de nivel secundario. """

# Funcion para cargar alumnos de un curso
def carga_nombres():
    lista_alumnos=[]
    alumno = input("Introduce el nombre de un alumno (x para salir): ")
    while alumno != 'x' and alumno != 'X':
        lista_alumnos.append(alumno)
        print("Alumno insertado.")
        alumno = input("Introduce el nombre de un alumno (x para salir): ")
    return lista_alumnos

# Funcion que coge dos listas y devuelve en función del argumento "reps", una lista completa con los elemenos no repetidos o con los repetidos
def busca_reps_listas(lista1,lista2,reps):
    lista_no_reps=lista2
    lista_reps=[]
    for elemento in lista1:
        if (elemento in lista_no_reps) == False:
            lista_no_reps = lista_no_reps + [elemento]
        else:
            lista_reps = lista_reps + [elemento]
    if reps == 0:
        return lista_no_reps
    else:
        return lista_reps

# Funcion que coge dos listas y devuelve en función del argumento "reps", una lista completa con los elemenos no repetidos o con los repetidos
def busca_reps_listas2(lista1,lista2,reps):
    lista_total = lista1 + lista2
    lista_no_reps=[]
    lista_reps=[]
    for elemento in lista_total:
        if lista_total.count(elemento)>1 and (elemento not in lista_reps):
            lista_reps.append(elemento)
        else:
            lista_no_reps.append(elemento)
    if reps==0:
        return lista_no_reps
    else:
        return lista_reps

def unicos_lista(lista1,lista2):
    lista_no_reps=[]
    for elemento in lista1:
        if elemento not in lista2:
            lista_no_reps.append(elemento)
    return lista_no_reps



#lista_a=("Pilar","Maria","Vicenta","Inma","Alicia","Natalia","Juncar")
#lista_b=("Natalia","Alicia","Sandra","Iris")

lista_a=carga_nombres()
lista_b=carga_nombres()
print("Lista sin repeticiones: "+str(busca_reps_listas2(lista_a,lista_b,0)))
print()
print("Lista de repetidos: "+str(busca_reps_listas2(lista_a, lista_b, 1)))
print()
print("Los elementos únicos de la primera lista son: "+str(unicos_lista(lista_a,lista_b)))

""" El ejercicio está planteado para hacerse de forma mucho más sencilla con conjuntos

def cargarNombres(alumnos):
   nombre=input("Nombre: ")
   while nombre!="x" and nombre != "X":
       alumnos.add(nombre)
       nombre=input("Nombre: ")
   return alumnos

lista_a = set()
lista_b = set()
print("ALUMNOS DE PRIMARIA")
lista_a=cargarNombres(lista_a)
print("ALUMNOS DE SECUNDARIA")
lista_b=cargarNombres(lista_b)

print("Unión: "+str(lista_a | lista_b))
print("Intesección: "+str(lista_a & lista_b))
print("Elementos únicos de la primera lista: "+str(lista_a-lista_b)) 

"""
