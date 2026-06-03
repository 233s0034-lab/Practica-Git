import re

class Expresion1:
    def ejecutar(self):

        # Expresión regular ({a} U {b}*)· {a}*· {bc}*
        exp = r'(a|b*)a*(bc)*'

        cadena = input('Ingresa una cadena:')
        res = re.fullmatch(exp, cadena)

        if res:
            print("La cadena", cadena, "sí coincide")
            print("Coincidencia:", res.group())
        else:
            print("La cadena", cadena, "no coincide")
