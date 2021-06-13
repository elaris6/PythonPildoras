# Pruebas CRUD (create, read, update, delete)
import sqlite3
import os

# Creación de datos
def creacion():
    miCursor.execute("""--sqlINSERT INTO PRODUCTOS VALUES (NULL,'avión',22,'juguetes')--endsql""")

# Lectura de datos
def lectura():
    seccion = 'juguetería'
    miCursor.execute(
        "SELECT * FROM PRODUCTOS WHERE PRECIO > 20 AND SECCION=?", (seccion,))
    resultadoQuery=miCursor.fetchall()
    print (len(resultadoQuery))
    print (resultadoQuery)

# Actualización de datos
def actualizacion():
    seccion = 'juguetería'
    miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 27 WHERE SECCION=?",(seccion,))
    resultadoQuery=miCursor.rowcount
    print (resultadoQuery)

# Borrado de datos
def borrado():
    miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO='pepe'")
    resultadoQuery=miCursor.rowcount
    print (resultadoQuery)

# Creamos la conexión con la BBDD
os.chdir(os.path.dirname(os.path.abspath(__file__)))

miConexion=sqlite3.connect("BBDD_pruebas_sqlite_2.db")
miCursor=miConexion.cursor()

# Función a usar
lectura()

# Aceptamos cambios y cerramos cursor y conexión
miConexion.commit()

miCursor.close()
miConexion.close()
