# Script para crear contraseñas aleatorias personalizables en cuanto a longitud y caracteres incluidos

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
symbols = "-_&$#*"

all = lower+upper+nums+symbols
lenght = 20

for i in range(5):
    password = "".join(random.sample(all,lenght))
    print(password)
