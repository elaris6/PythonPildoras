# Prueba con creación de BBDD y tabla con clave primaria
import sqlite3
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

miConexion=sqlite3.connect("BBDD_pruebas_sqlite_2.db")
miCursor=miConexion.cursor()

# Creación de tabla con PK e inserción de registros en bloque y uno separado
"""
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))  
''')

productos=[
    ("AR01", "pelota", 20, "jugeteria"),
    ("AR02", "pantalón", 15, "confección"),
    ("AR03", "destornillador", 25, "ferretería"),
    ("AR04", "jarrón", 45, "cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?, ?, ?, ?)", productos)

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','camion',12,'juguetes')")
"""

# Creación de tabla con PK autonicremental, otro campo único e inserción de registros en bloque y uno separado,
# probando la inserción con PK y la restricción de campo único UNIQUE
"""
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    CODIGO_ARTICULO INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))  
''')

productos=[
    ("pelota", 20, "jugeteria"),
    ("pantalón", 15, "confección"),
    ("destornillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL, ?, ?, ?)", productos)
"""
#miCursor.execute("INSERT INTO PRODUCTOS VALUES (NULL,'camion',12,'juguetes')")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES (NULL,'pelota',12,'juguetes')")

#miConexion.commit()

miCursor.execute("SELECT * FROM PRODUCTOS")

resultadoQuery=miCursor.fetchall()
print (resultadoQuery)
print("--------------------------------------------")
for i in range(4):
    for j in range(4):
        print(resultadoQuery[i][j])
print("--------------------------------------------")
print(resultadoQuery[0][0])
miCursor.close()
miConexion.close()
