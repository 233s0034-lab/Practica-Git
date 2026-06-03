import re

class Expresion3:
    def ejecutar(self):

        # ({a U b U ... U 0 U 1 U ... U _})+
        nombre = r'[a-zA-Z0-9_]+'  

        # {pdf U docx U txt}
        extension = r'(pdf|docx|txt)'

        # ({/users/ U /home/})· nombre· {.}· extension
        archivo = r'/(users|home)/' + nombre + r'\.' + extension

        # {0 U 1 U 2 U 3 U 4 U 5 U 6 U 7 U 8 U 9}
        ip = r'[0-9]{1,3}(\.[0-9]{1,3}){3}'

        # nombre · {@} · IP
        destino = nombre + r'@' + ip

        # ({/users/ U /home/})· ({a U b ... U /})+
        ruta = r'/(users|home)/[a-zA-Z0-9_/]+'

        # {copy} · {espacio} · archivo · {espacio} · destino · {:} · ruta
        patron = r'copy' + r' ' + archivo + r' ' + destino + r':' + ruta

        cadena = input("Ingrese el comando: ")

        if re.fullmatch(patron, cadena):
            print(f'El comando "{cadena}" si es valido')
        else:
            print(f'El comando "{cadena}" no es valido')



