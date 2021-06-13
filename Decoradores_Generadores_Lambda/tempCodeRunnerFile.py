lista = ['Hola','Adios','Buenos días']
elem = 'saludos'

if elem.upper() in [elem.upper() for elem in lista]:
    print('Encontrada')
else:
    print('No encontrada')