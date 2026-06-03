while True:
    print("\n--- MENÚ ---")
    print("1. Expresión (a|b*)a*(bc)*")
    print("2. Dirección IP")
    print("3. Comando ruta")
    print("4. Expresión (A|a)*(a|b)*ba*")
    print("5. Expresión b*ab*")
    print("6. Expresión b(a|b)*")
    print("7. Expresión (a|b)*ba(a|b)*")
    print("8. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            from expresion1 import Expresion1
            obj = Expresion1()
            obj.ejecutar()
        case "2":
            from expresion2 import Expresion2
            obj = Expresion2()
            obj.ejecutar()
        case "3":
            from expresion3 import Expresion3
            obj = Expresion3()
            obj.ejecutar()
        case "4":
            from expresion4 import Expresion4
            obj = Expresion4()
            obj.ejecutar()
        case "5":
            from expresion5 import Expresion5
            obj = Expresion5()
            obj.ejecutar()
        case "6":
            from expresion6 import Expresion6
            obj = Expresion6()
            obj.ejecutar()
        case "7":
            from expresion7 import Expresion7
            obj = Expresion7()
            obj.ejecutar()
        case "8":
            print("Saliendo...")
            break
        case _:
            print("Opcion no valida")
