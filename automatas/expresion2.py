import re

class Expresion2:
    def ejecutar(self):

        # D = {0 U 1 U 2 U 3 U 4 U 5 U 6 U 7 U 8 U 9}
        # Expresión regular: (D · (D U ε) · (D U ε)) · {.} · (D · (D U ε) · (D U ε)) · {.} · {1} · {.} · {1}

        patron = r'[0-9]{1,3}\.[0-9]{1,3}\.1\.1'

        cadena = input("Ingrese la direccion IP: ")

        if not re.fullmatch(patron, cadena):
            print("La direccion IP", cadena, "no es valida")
            return False

        partes = cadena.split('.')

        for i in range(2):
            if int(partes[i]) < 0 or int(partes[i]) > 255:
                print("La direccion IP", cadena, "no es valida")
                return False

        print("La direccion IP", cadena, "si es valida")
        return True


