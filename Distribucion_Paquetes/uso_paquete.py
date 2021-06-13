"""
Uso del paquete custom instalado en local

Dependiendo de si lo que hemos instalado es un paquete (con subpaquetes) o un módulo,
la forma de acceder será distinta

"""
# importamos el paquete (que no tiene objetos directamente accesibles)
import paquete 
# Importamos un módulo del paquete raíz
import paquete.funcionesMatematicas 
# Importamos un módulo de un sub paquete
from paquete.sub_paquete.funcionesMatematicasAvanzadas import *

paquete.funcionesMatematicas.sumar(2, 3)

raiz(144,2)

#help(paquete)


