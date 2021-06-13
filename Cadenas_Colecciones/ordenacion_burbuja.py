lista = [16,4,76,98,4,6,456,786,8,1,45,7,8,9,243,]

for i in range (len(lista)-1):
    for j in range (len(lista)-1):
        if lista[j] > lista[j+1]:
            lista[j],lista[j+1] = lista[j+1],lista[j]

print(lista)