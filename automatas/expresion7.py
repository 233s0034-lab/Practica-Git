import re

class Expresion7:
    def ejecutar(self):

        # (a U b)* ba (a U b)*
        # Expresión regular: ({a} U {b})* · {b} · {a} · ({a} U {b})*
        exp = r'(a|b)*ba(a|b)*'

        cadena = input('Ingresa una cadena:')
        res = re.fullmatch(exp, cadena)

        if res:
            print("La cadena", cadena, "sí coincide con la expresión")
            print("Coincidencia:", res.group())
        else:
            print("La cadena", cadena, "no coincide con la expresión")


