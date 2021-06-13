import re

""" match busca desde el principio coincidencia con un patrón (incluyendo RegEx) en una cadena """

nombre1='Claudia López'
nombre2='Claudio Pérez'
nombre3='Jara López'
nombre4='Lara González'
cadena1='456435645'
cadena2='a45643563'
cadena3='546560564'

if re.match('Claudi.',nombre1): # re.match('claudi.',nombre1,re.IGNORECASE) para que no sea CASE sensitive
    print('Encontrado')
else:
    print('No encontrado')

if re.match('.ara', nombre4):
    print('Encontrado')
else:
    print('No encontrado')

if re.match('\d', cadena2): # Comienza por un dígito
    print('Encontrado')
else:
    print('No encontrado')

""" search busca coincidencia con un patrón (incluyendo RegEx) en una cadena, no necesariamente al principio """

if re.search('López', nombre1):
    print('Encontrado')
else:
    print('No encontrado')

if re.search('64', cadena3):
    print('Encontrado')
else:
    print('No encontrado')
