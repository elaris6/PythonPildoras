"""
Descripción de un paquete distribuible
Una vez creado, ejecutar desde consola "python setup.py dist"
"""


from setuptools import setup

setup(
    name="funcionesMatematicasBasicas",
    version="1.0", #no sigue estructura definida
    description="Esto es un ejemplo para ver los paquetes distribuibles",
    author="elaris6",
    packages=["Modulos","Modulos.paquete_prueba.sub_paquete_prueba"]

)