import sqlite3
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

miConexion=sqlite3.connect("BBDD_pruebas_sqlite.db")
miCursor=miConexion.cursor()

miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR (20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")
"""
variosProductos=[
    ("CAMISETA",10,"TEXTIL"),
    ("JARRON",25,"BAZAR"),
    ("SILLA",30,"JARDIN"),
    ("COCHE",15,"JUGUETES")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)

miConexion.commit()
"""
miCursor.execute("SELECT * FROM PRODUCTOS")

resultadoQuery=miCursor.fetchall()
print (resultadoQuery)
resultadoQuery=miCursor.fetchone() 
print (resultadoQuery) # El cursor queda vacío si ya ha devuelto todos los registros



miCursor.close()
miConexion.close()
