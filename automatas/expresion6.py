import re

class Expresion6:
    def ejecutar(self):

        # b(a U b)* 
        # Expresión regular: {b} · ({a} U {b})*
        exp = r'b(a|b)*'

        cadena = input('Ingresa una cadena:')
        res = re.fullmatch(exp, cadena)

        if res:
            print("La cadena", cadena, "sí coincide con la expresión")
            print("Coincidencia:", res.group())
        else:
            print("La cadena", cadena, "no coincide con la expresión")



