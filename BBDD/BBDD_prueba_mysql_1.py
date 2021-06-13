from mysql.connector import errorcode
import mysql.connector

""" Opción de conexión con parámetros

config = {
  'user': 'scott',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

"""

try:
    # El atributo database es opcional, pero habrá que indicar el esquema
    conexion = mysql.connector.connect(
        user='dbuser', password='AliNata0', host='localhost', database='sakila')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Nombre de usuario o contraseña incorrectos.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La BBDD a la que intenta conectar no existe")
    else:
        print(err)


cursor = conexion.cursor()
query = """SELECT * FROM actor"""

cursor.execute(query)

resultados = cursor.fetchall()

for resultado in resultados:
    print(resultado[2])


conexion.close()
