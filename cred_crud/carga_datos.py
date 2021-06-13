# Script para poblar la BBDD sqlite de cred_crud con registros de pruebas

import sqlite3
import random
import os

# Deinimos directorio de trabajo
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Abrimos conexión con la BBDD sqlite
conexion_bbdd = sqlite3.connect("cred_crud.sqlite")
cursor_bbdd = conexion_bbdd.cursor()

descBuscar="%entorno%"
cursor_bbdd.execute('''--sql
                    SELECT * FROM CREDENCIALES WHERE DESCRIPCION LIKE ?
                    --endsql''',(descBuscar,))
resultadoQuery = cursor_bbdd.fetchall()

print (len(resultadoQuery))
for registro in resultadoQuery:
    print(registro)

"""
for i in range(10):
    aleatNum = random.randint(0, 100)
    cursor_bbdd.execute('''--sql
        INSERT INTO CREDENCIALES VALUES (NULL,?,?,?,?)
        --endsql''', (f"Entorno{aleatNum}",
                    f"Usuario{aleatNum}",
                    f"Contraseña{aleatNum}",
                    f"Esto es un registro de prueba {aleatNum}"))
"""

cursor_bbdd.close()
conexion_bbdd.close()



