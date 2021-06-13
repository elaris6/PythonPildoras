#https://docs.hektorprofe.net/python/manejo-de-ficheros/ejercicios/
# ejercicio 3

import pickle
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class ErrorPersonaje(Exception):
    pass

class Personaje():

    def __init__(self,clase,vida,ataque,defensa,alcance):

        try:
            self.clase = clase
            self.vida = int(vida)
            self.ataque = int(ataque)
            self.defensa = int(defensa)
            self.alcance = int(alcance)
        except ErrorPersonaje:
            pass
        if (vida<1) or (ataque<1) or (defensa<1) or (alcance < 1):
            raise ErrorPersonaje

class Gestor():
    
    def __init__(self):
        
        fichero=open('personajes.pckl','ab+')
        fichero.seek(0)
        try:
            self.lista_personajes=pickle.load(fichero)
        except:
            #El fichero está vacío
            self.lista_personajes=[]
        finally:
            fichero.close()
            print("Se han cargado {} personajes almacenados".format(len(self.lista_personajes)))

    def guardar(self):
        fichero = open('personajes.pckl', 'wb')
        pickle.dump(self.lista_personajes, fichero)
        fichero.close()

    def mostrar(self):

        if len(self.lista_personajes) == 0:
            print("El fichero está vacío")
        else:
            for personaje in self.lista_personajes:
                print(f'{personaje.clase} =>\tVida: {personaje.vida}\t\tAtaque: {personaje.ataque}\tDefensa: {personaje.defensa}\tAlcance: {personaje.alcance} ')
    
    def crear(self):
        print("Introduce la clase y atributos del nuevo personaje:")
        clase=input("Clase [Caballero | Guerrero | Arquero]: ")
        clase_repe=False
        for personaje in self.lista_personajes:
            if personaje.clase == clase:
                clase_repe=True
                break
        if clase_repe:
            print("Esa clase ya existe en el gestor de personajes.")
            raise ErrorPersonaje

        vida=int(input("Vida [Entero mayor que cero]: "))
        ataque = int(input("Ataque [Entero mayor que cero]: "))
        defensa = int(input("Defensa [Entero mayor que cero]: "))
        alcance = int(input("Alcance [Entero mayor que cero]: "))

        try:
            pTemp=Personaje(clase,vida,ataque,defensa,alcance)
            self.lista_personajes.append(pTemp)
            self.guardar()
            print("Clase creada!")
        except:
            print("Error en creación de personaje. Revise atributos.")

    def borrar(self):
        print("Introduce la clase a borrar:")
        clase = input("Clase [Caballero | Guerrero | Arquero]: ")
        clase_found=False
        for personaje in self.lista_personajes:
            if personaje.clase == clase:
                clase_found = True
                self.lista_personajes.remove(personaje)
                self.guardar()
                print("Clase borrada!")
                break
        if not clase_found:
            print("Esa clase no existe en el gestor de personajes.")

g=Gestor()
#g.crear() # x3 para crear cada personaje
g.mostrar()
#g.borrar() # borrar un personaje
#g.mostrar()

"""
fichero = open("personajes.pckl", "rb")  # read binary
lista = pickle.load(fichero)
print(lista)
"""
