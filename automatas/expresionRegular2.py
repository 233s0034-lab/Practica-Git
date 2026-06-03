import re

def validar_expresion2():
    
    patron = r'copy /[a-zA-Z0-9_/]+\.pdf [a-zA-Z0-9_]+@[0-9]{1,3}(\.[0-9]{1,3}){3}:/[a-zA-Z0-9_/]+'
    
    cadena = input("Ingrese el comando: ")
    
    if re.fullmatch(patron, cadena):
        print(f'El comando "{cadena}" sí es valido')
    else:
        print(f'El comando "{cadena}" no es valido')

validar_expresion2()
