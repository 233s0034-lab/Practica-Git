import re

class Expresion4:
    def ejecutar(self):

        # Expresión regular: ({A} U {a})* · ({a} U {b})* · {ba}*
        exp = r'(A|a)*(a|b)*ba*'

        cadena = input('Ingresa una cadena:')
        res = re.fullmatch(exp, cadena)

        if res:
            print("La cadena", cadena, "si coincide con la expresion")
            print("Coincidencia:", res.group())
        else:
            print("La cadena", cadena, "no coincide con la expresion")



