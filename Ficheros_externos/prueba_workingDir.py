import os

# https://note.nkmk.me/en/python-script-file-path/


print("-----------------------------------------------------")
print ('Salida de os.getcwd(): ',os.getcwd())
print('Salida de __file__: ',__file__)
print('Nombre fichero en ejecución: ', os.path.basename(__file__))
print('Directorio fichero en ejecución: ', os.path.dirname(__file__))
print('abspath:     ', os.path.abspath(__file__))
print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))
print("-----------------------------------------------------")
print('Cambiamos directorio de ejecución al del fichero actual')
# Modificar directorio os.chdir()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print('Salida de os.getcwd(): ', os.getcwd())
print("-----------------------------------------------------")
