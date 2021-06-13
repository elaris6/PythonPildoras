def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	try:
		return num1/num2
	except ZeroDivisionError:
		print("Error al intnetar dividir por cero.")
		return ""
	
# Bloque principal del programa	
while True:
	try:
		op1 = int((input("Introduce el primer número: ")))
		op2 = int((input("Introduce el primer número: ")))
		break
	except ValueError:
		print("Valor introducido no numérico. Inténtalo de nuevo.")
"""	except ErrorControladoN:
		pass
	finally: #Se ejecuta siempre, haya error o no.
		pass """


operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")
if operacion=="suma":
	print(suma(op1,op2))
elif operacion=="resta":
	print(resta(op1,op2))
elif operacion=="multiplica":
	print(multiplica(op1,op2))
elif operacion=="divide":
	print(divide(op1,op2))
else:
	print ("Operación no contemplada")


print("Proceso finalizado. Continuación de ejecución del programa ")
