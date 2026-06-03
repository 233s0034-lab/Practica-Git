from calificaciones import Calificaciones
import tkinter as tk
from tkinter import filedialog

ruta_archivo = filedialog.askopenfilename(
    title="Seleccione el archivo de texto",
    filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")),
)

if not ruta_archivo:
    print("No se seleccionó archivo.")
    exit()

print(f"Archivo seleccionado: {ruta_archivo}")

obj = Calificaciones(ruta_archivo)

while True:
    print("\n--- MENÚ ---")
    print("1. Contenido")
    print("2. Agregar registro")
    print("3. Modificar calificación")
    print("4. Eliminar registros")
    print("5. Ordenar por nombre")
    print("6. Ordenar por calificación")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            obj.visualizar()
        case "2":
            obj.agregar()
        case "3":
            obj.modificar()
        case "4":
            obj.eliminar()
        case "5":
            obj.ordenarNombre()
        case "6":
            obj.ordenarCalif()
        case "7":
            print("Saliendo...")
            break
        case _:
            print("Opcion no valida")
