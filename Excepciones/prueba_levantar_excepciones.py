import math

def calculaRaiz (num):
    if num < 0:
        raise ValueError ("El número no puede ser negativo.")
    else:
        return math.sqrt(num)

#Bloque principal del pgrama
userNum=(int(input("Introduce un número: ")))

try:
    print(calculaRaiz(userNum))
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)

print("Prgrama finalizado :)")
