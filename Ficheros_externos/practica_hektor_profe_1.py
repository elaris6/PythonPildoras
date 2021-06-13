#https://docs.hektorprofe.net/python/manejo-de-ficheros/ejercicios/
# ejercicio 1

personas=[]
with open('personas.txt','r',encoding='utf8') as file:
    for line in file:
        line=line.replace('\n','')
        line=line.split(';')
        persona = {'ID': line[0], 'nombre': line[1],
                   'apellido': line[2], 'fechaNac': line[3]}

        personas.append(persona)

for persona in personas:
    print('(id={}) {} {} FN={}'.format(
        persona['ID'], persona['nombre'], persona['apellido'], persona['fechaNac']))
    
