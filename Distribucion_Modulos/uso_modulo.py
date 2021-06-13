"""
Uso del paquete custom instalado en local

Dependiendo de si lo que hemos instalado es un paquete (con subpaquetes) o un módulo,
la forma de acceder será distinta

"""
# Importamos nuestro módulo de la raíz
import funcionesMatematicas 
# Importamos nuestro módulo de la sub_carpeta
import sub_carpeta.funcionesMatematicasAvanzadas  

funcionesMatematicas.sumar(6,17)
sub_carpeta.funcionesMatematicasAvanzadas.raiz(9,2)

#help(funcionesMatematicas)
#help(sub_carpeta.funcionesMatematicasAvanzadas)


