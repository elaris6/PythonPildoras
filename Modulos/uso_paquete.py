# paquete prueba es la carpeta con los modulos a importar
from paquete_prueba.funcionesMatematicas import sumar
# se pueden indicar subcarpetas que sean paquetes anidados con la nomenclatura del punto
from paquete_prueba.sub_paquete_prueba.funcionesMatematicasAvanzadas import raiz

sumar(12, 7)
raiz(144,2)

