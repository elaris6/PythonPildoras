print("\nOperaciones:\n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n")
operando1 = int(input("Operando 1: "))
operando2 = int(input("Operando 2: "))
operacion = int(input("Tipo operación: "))

if operacion == 1:
    resultado = operando1+operando2
    print ("\nSuma: ",resultado)
elif operacion == 2:
    resultado=operando1-operando2
    print("\nResta: ", resultado)
elif operacion == 3:
    resultado=operando1*operando2
    print("\nMultiplicación: ", resultado)
elif operacion == 4:
    try:
        resultado=operando1/operando2
        print("\nDivisión: ", resultado)
    except ZeroDivisionError:
        print("\nDivisón por cero no permitida.")

