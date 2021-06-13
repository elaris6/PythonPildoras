import pickle

# Creación de fichero serializado

"""
lista_nombres=["Mari","Isra","Alicia","Natalia","Vicen","Rubén"]

fichero_binario=open("lista_nombres","wb") # write binary

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()

del(fichero_binario) # limpiar la memoria, no borra el fichero físico
"""

# Lectura fichero serializado

fichero=open("lista_nombres","rb") # read binary

lista=pickle.load(fichero)

print(lista)
