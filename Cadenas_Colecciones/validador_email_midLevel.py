""" Script que validará si una cadena introducida es un email válido o no. """

def check_arroba(email):
    # Validamos que la dirección tenga una arroba y que no esté al principio o al final de la cadena
    pos_arroba=email.find("@")
    if pos_arroba<0:
        return False,"","","Formato no válido. No se ha introducido el caracter @ para deliminar usuario y dominio."
    elif email.count("@")>1:
        return False,"","","Formato incorrecto. Se ha introducido el caracter @ más de una vez."
    elif pos_arroba==0:
        return False,"","","Formato no válido. No se ha introducido el nombre de usuario del email."
    elif pos_arroba==(len(email)-1):
        print()
        return False,"","","Formato incorrecto. No se ha introducido el dominio del email."
    else:
        # Si la comprobación de la arroba es ok, dividimos el email en usuario y dominio y lo retornamos
        usuario=email[0:pos_arroba]
        dominio=email[pos_arroba+1:len(email)]
        return True,usuario,dominio,"Validación arroba correcta."

def check_user(usuario):
    # Comprobamos longitud de la parte usuario
    if len(usuario)>64:
        print("La longitud del usuario excede el máximo admitido.")
        return False
    # Comprobamos si la parte usuario contiene algún caracter no admitido
    allowed_char_user="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_"

    for c in usuario:
        if c not in allowed_char_user:
            print("La parte usuario contiene algún caracter no admitido.")
            return False
    return True

def check_domain(dominio):
    # Comprobamos longitud de la parte dominio
    pos_punto=dominio.rfind(".")
    if len(dominio)>255:
        print("La longitud del dominio excede el máximo admitido.")
        return False
    # Comprobamos si la parte usuario contiene algún caracter no admitido
    allowed_char_domain="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_"

    for c in dominio:
        if c not in allowed_char_domain:
            print("La dominio contiene algún caracter no admitido.")
            return False    

    if pos_punto<0:
        return False
    elif pos_punto==0:
        return False
    elif pos_punto==(len(dominio)-1):
        print()
        return False
    else:
        dom_name=dominio[0:pos_punto]
        dom_ext=dominio[pos_punto+1:len(dominio)]
        print("Nombre domino: ",dom_name,"\nExtensión dominio: ",dom_ext)
        if len(dom_ext)<2:
            print("Extensión de dominio formato incorrecto. Longitud insuficiente.")
            return False
        elif len(dom_name)<2:
            print("Extensión de dominio formato incorrecto. Longitud insuficiente.")
            return False
        return True

""" Bloque principal del programa """

email="pru-eba@do.main.es"
#email=input("por favor, introduce una dirección de email: ")

arroba,usuario,dominio,mensaje=check_arroba(email)

if arroba == False:
    print(mensaje)
elif check_user(usuario) == False:
    print()
elif check_domain(dominio)==False:
    print()
else:
    print("--- Las comprobaciones realizadas sobre el email introducido son correctas!")
    print("Usuario: ",usuario,"\nDominio: ",dominio)
    print("--- Fin")

