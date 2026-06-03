import re

while True:
    print("\n--- MENÚ ---")
    print("1. Expresión regular b(a|b)*a")
    print("2. Expresion regular ((a|b)(a|b))*")
    print("3. Expresion regular 1*01*01*")
    print("4. Expresion regular (0|1)*0(0|1)")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        patron = r"b(a|b)*a"
        cadena = input("Ingrese la cadena: ")

        if re.fullmatch(patron, cadena):
            print("La cadena ", cadena, " si es valida")
        else:
            print("La cadena ", cadena, " no es valida")

    elif opcion == "2":
        patron = r"((a|b)(a|b))*" 
        cadena = input("Ingrese la cadena: ")

        if re.fullmatch(patron, cadena):
            print("La cadena", cadena, " tiene longitud par")
        else:
            print("La cadena", cadena, " no tiene longitud par")

    elif opcion == "3":
        patron = r"1*01*01*"
        cadena = input("Ingrese la cadena: ")

        if re.fullmatch(patron, cadena):
            print("La cadena", cadena, " tiene exactamente dos ceros")
        else:
            print("La cadena", cadena, " no tiene dos ceros")

    elif opcion == "4":
        patron = r"(0|1)*0(0|1)"
        cadena = input("Ingrese la cadena: ")

        if re.fullmatch(patron, cadena):
            print("El penúltimo símbolo de la cadena", cadena, " es 0")
        else:
            print("La cadena", cadena, " no es valida")

    elif opcion == "5":
        print("Programa cerrado")
        break

    else:
        print("Opción no valida")
