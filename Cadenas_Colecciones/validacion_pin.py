import random
import time

def validation(pin):
    global secret
    if pin == secret:
        return 0
    else:
        return 1

secret = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
print('El PIN es muy secreto, es: '+secret)
print ('Introduzca su número secreto (3 intentos):')
for i in range(1,4):
    while True:
        user_pin= str(input('PIN 4 posiciones: '))
        if len(user_pin) < 4:
            print('Formato PIN incorrecto. Longitud inferior a 4')
        elif len(user_pin) > 4:
            print('Formato PIN incorrecto. Longitud superior a 4')
        else:
            break
    
    time.sleep(1)
    if validation(user_pin) == 0:
        print('PIN CORRECTO')
        break
    elif i<3:
        print('PIN incorrecto. Vuelva a introducir PIN.')
    else:
        print('PIN incorrecto. No le quedan más intentos')


