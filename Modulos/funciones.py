""" Cometarios de este módulo.
    Este módulo contiene operaciones matemáticas básicas
"""

def sumar(op1,op2):
    print ("El resultado de la suma es: ", str(op1+op2))

def restar(op1,op2):
    print ("El resultado de la resta es: ", str(op1-op2))

def multiplicar(op1,op2):
    print ("El resultado de la multiplicación es: ", str(op1*op2))

def dividir(op1,op2):
    if op2==0:
        print("No se puede dividir por cero.")
    else:
        print ("El resultado de la division es: ", str(op1/op2))


