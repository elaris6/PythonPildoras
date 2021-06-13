import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva ",self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:

    personas=[]

    def __init__(self):
        listaDePersonas=open("ficheroPersonas","ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print("se cargaron {} personas del fichero de guardado.".format(len(self.personas)))
        except:
            print("Fichero creado vacío.")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)


    def agregarPersona(self,persona):
        self.personas.append(persona)
        self.guardarPersonasEnFichero()
        print("Se ha agregado ",persona.nombre," a la lista.")

    def mostratPersonas(self):
        for persona in self.personas:
            print(persona)

    def guardarPersonasEnFichero(self):
        listaDePersonas=open("ficheroPersonas","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarPersonasFichero(self):
        print("La lista de personas almacenadas en el fichero es la siguiente:")
        for persona in self.personas:
            print(persona)



# Código para crear, almacenar y recuperar personas de un fichero externo de almacenamiento
listaP=ListaPersonas()

# En esta parte estaríamos creando y guardando personas
"""
p1=Persona("Alicia","Femenino",9)
listaP.agregarPersona(p1)
p1=Persona("Natalia","Femenino",6)
listaP.agregarPersona(p1)
p1=Persona("Mari","Femenino",39)
listaP.agregarPersona(p1)
p1=Persona("Israel","Masculino",41)
listaP.agregarPersona(p1)
"""

listaP.mostrarPersonasFichero()




