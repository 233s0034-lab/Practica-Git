import re

class Expresion5:
    def ejecutar(self):

        # b*ab* = (b*) · (a) · (b*)
        # Expresión regular: {b}* · {a} · {b}*
        exp = r'b*ab*'

        cadena = input('Ingresa una cadena:')
        res = re.fullmatch(exp, cadena)

        if res:
            print("La cadena", cadena, "sí coincide con la expresión")
            print("Coincidencia:", res.group())
        else:
            print("La cadena", cadena, "no coincide con la expresión")



