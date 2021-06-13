import sqlite3
import os

# Cambiamos directorio de trabajo
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Creamos la conexión 
miConexion=sqlite3.connect("instanciaBBDD.db") # Si la BBDD no existe, la crea

# Creamos cursor en la conexión
miCursor=miConexion.cursor()

# Realizamos las gestiones que deseemos contra la BBDD abierta
#miCursor.execute("CREATE TABLE TABLA1 (CAMPO1 INTEGER, CAMPO2 VARCHAR(20), CAMPO3 VARCHAR(10))")
miCursor.execute("""--sql
INSERT INTO TABLA1 VALUES(1,'INFO1','INFO2')
--endsql""")
miConexion.commit()



miConexion.close()
