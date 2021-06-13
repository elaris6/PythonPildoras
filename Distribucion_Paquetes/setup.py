"""
Plantilla base para la configuración de la función setup

INFO COMPLETA: https://docs.hektorprofe.net/python/distribucion/setuptools/
INFO OFICIAL: https://docs.python.org/3/distutils/setupscript.html

"""
from setuptools import setup

setup(name="Paquete Prueba",  # Nombre
      version="0.1",  # Versión de desarrollo
      description="Paquete de prueba",  # Descripción del funcionamiento
      author="Nombre Autor",  # Nombre del autor
      author_email='prueba@prueba.com',  # Email del autor
      license="GPL",  # Licencia: MIT, GPL, GPL 2.0...
      url="http://ejemplo.com",  # Página oficial (si la hay)
      packages=['paquete','paquete.sub_paquete'], # Para crear paquetes con subpaquetes
      #py_modules=['funcionesMatematicas'], # Para crear módulos instalables (directamente en la misma ruta que setup.py)
      )

"""
SUB PAQUETES
Para el caso de que haya muchos subpaquetes, se puede usar la función find_packages

from setuptools import setup, find_packages
setup(...
      packages=find_packages()
)

DEPENDENCIAS EXTERNAS

# Se instala la versión más actual
setup(...,
      install_requires=["pillow"],
)

# Se instala la versión exacta indicada
setup(...,
      install_requires=["pillow==1.1.0"],
)

# Se instala la versión igual o superior a la indicada
setup(...,
      install_requires=["pillow>=1.1.5"],
)

MUCHAS DEPENDENCIAS

Creamos fichero "requirements.txt" con contenido de ejemplo:
pillow==1.1.0
django>=1.10.0,<=1.10.3
pygame

y en el fichero setup.py se indica:

setup(...,
      install_requires=[i.strip() for i in open("requirements.txt").readlines()],
)

SUITE TEST

| setup.py
| requeriments.txt
+ prueba/          
   | __init__.py   
   | modulo.py  
+ tests/
   | __init__.py   
   | test_pillow.py
   | test_django.py
   | test_pygame.py

setup(...,
      test_suite="tests"
)

c:\>python setup.py test

PRUEBA PAQUETE

# Instalación para pruebas
python setup.py develop [--uninstall]

# Instalación definitiva. Para modificar funcionamiento hay que reinstalar con PIP
python setup.py install

DISTRIBUCION PAQUETE

# Crear comprimido para distribuir localmente
python setup.py sdist

# Instalación del paquete en otro entorno local
pip install nombre_del_fichero.zip  


"""
