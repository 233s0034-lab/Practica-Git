class Calificaciones:

    def __init__(self, ruta):
        self.ruta = ruta

    def visualizar(self):
        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo:
                print("\n--- CONTENIDO DEL ARCHIVO ---")
                contenido = archivo.read()
                print(contenido if contenido else "(Archivo vacío)")
        except FileNotFoundError:
            print("El archivo no existe.")

    def agregar(self):

        nombre = input("Nombre: ")
        asignatura = input("Asignatura: ")
        calif = input("Calificación: ")

        with open(self.ruta, "rb+") as archivo:

            archivo.seek(0, 2)

            if archivo.tell() > 0:
                archivo.seek(-1, 2)
                ultimo = archivo.read(1)

                if ultimo != b"\n":
                    archivo.write(b"\n")

        with open(self.ruta, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre} {asignatura} {calif}\n")

        print("Registro agregado.")

    def modificar(self):

        nombre = input("Nombre a modificar: ")
        nueva = input("Nueva calificación: ")

        modificado = False

        with open(self.ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        with open(self.ruta, "w", encoding="utf-8") as archivo:

            for linea in lineas:

                partes = linea.strip().split()

                if len(partes) == 3 and partes[0] == nombre:
                    archivo.write(f"{partes[0]} {partes[1]} {nueva}\n")
                    modificado = True
                else:
                    archivo.write(linea)

        if modificado:
            print("Registro modificado.")
        else:
            print("No se encontró el registro.")

    def eliminar(self):

        nombre = input("Nombre a eliminar: ")
        encontrado = False

        with open(self.ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        with open(self.ruta, "w", encoding="utf-8") as archivo:

            for linea in lineas:

                partes = linea.strip().split()

                if len(partes) >= 1 and partes[0] == nombre:
                    encontrado = True
                else:
                    archivo.write(linea)

        if encontrado:
            print("Registro eliminado.")
        else:
            print("No se encontró.")

    def ordenarNombre(self):

        with open(self.ruta, "r", encoding="utf-8") as archivo:
            registros = [line.strip() for line in archivo if line.strip()]

        registros.sort(key=lambda x: x.split()[0].lower())

        with open(self.ruta, "w", encoding="utf-8") as archivo:
            archivo.write("\n".join(registros) + "\n")

        print("Ordenado por nombre.")

    def ordenarCalif(self):

        with open(self.ruta, "r", encoding="utf-8") as archivo:
            registros = [line.strip() for line in archivo if line.strip()]

        registros.sort(key=lambda x: float(x.split()[2]))

        with open(self.ruta, "w", encoding="utf-8") as archivo:
            archivo.write("\n".join(registros) + "\n")

        print("Ordenado por calificación.")
