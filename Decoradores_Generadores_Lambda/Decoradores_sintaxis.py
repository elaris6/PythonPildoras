""" Ejemplo funciones decoradoras """

"""
En los parámetros de la función interna y de la función parámetro se pueden indicar
las convenciones *args y **kwargs, para que se adapten a cualquier tipo de argumento recibido.
"""

def funcion_decoradora(funcion_parametro):
    def funcion_interna(*args,**kwargs):
        # Acciones adicionales que agregan
        print("Vamos a realizar un cálculo con la función {}!".format(funcion_parametro.__name__))
        funcion_parametro(*args,**kwargs)

        # Accciones adicionales que agregan más
        print("Hemos terminado el cálculo con la función {}!".format(funcion_parametro.__name__))
    
    return funcion_interna


@funcion_decoradora
def suma(num1,num2):
    print(num1+num2)

@funcion_decoradora
def cuadrado(num):
    print(num**2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

@funcion_decoradora
def muestra_valor(elemento):
    print(elemento['clave'])

@funcion_decoradora
def saludar():
    print("Decorando!")

suma(15,20)
muestra_valor({'clave':'valor'})
cuadrado(5)
potencia(base=4, exponente=4)
saludar()
