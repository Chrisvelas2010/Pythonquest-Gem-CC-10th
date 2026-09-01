# ==========================================
# PYTHON QUEST
# PROYECTO FINAL
# Simulador de Gestión de Reinos y Batallas
# ==========================================


# ==========================================
# MÓDULO 1 — CLASE UNIDAD
# ==========================================

class Unidad:
    def __init__(self, nombre, tropas, potencia):
        self.nombre = nombre
        self.tropas = tropas
        self.potencia = potencia

    def atacar(self, enemigo):
        danio = self.potencia * 5
        enemigo.tropas -= danio

        if enemigo.tropas < 0:
            enemigo.tropas = 0

        print(f"{self.nombre} atacó a {enemigo.nombre}.")
        print(f"{enemigo.nombre} tiene {enemigo.tropas} tropas restantes.")

    def mostrar_estado(self):
        print(f"{self.nombre} | Tropas: {self.tropas} | Potencia: {self.potencia}")


# ==========================================
# MÓDULO 2 — CLASE REINO
# ==========================================

class Reino:
    def __init__(self, nombre, oro):
        self.nombre = nombre
        self.oro = oro
        self.ejercito = []

    def reclutar_unidad(self, nueva_unidad, costo):
        if self.oro >= costo:
            self.oro -= costo
            self.ejercito.append(nueva_unidad)

            print(f"{nueva_unidad.nombre} fue reclutada para {self.nombre}.")
            print(f"Costo: {costo} de oro.")
        else:
            print(f"{self.nombre} no tiene suficiente oro.")

    def mostrar_reino(self):
        print("\n=== ESTADO DEL REINO ===")
        print(f"Reino: {self.nombre}")
        print(f"Oro disponible: {self.oro}")

        print("\nEjército:")

        if len(self.ejercito) == 0:
            print("No hay unidades reclutadas.")
        else:
            for unidad in self.ejercito:
                unidad.mostrar_estado()


# ==========================================
# MÓDULO 3 — PERSISTENCIA Y VALIDACIÓN
# ==========================================

def guardar_partida(reino):
    try:
        with open("partida.txt", "w") as archivo:
            archivo.write(f"{reino.nombre}\n")
            archivo.write(f"{reino.oro}\n")
            archivo.write(f"{len(reino.ejercito)}\n")

            for unidad in reino.ejercito:
                archivo.write(
                    f"{unidad.nombre}|{unidad.tropas}|{unidad.potencia}\n"
                )

        print("Partida guardada correctamente.")

    except Exception as error:
        print("No se pudo guardar la partida.")
        print("Error:", error)


def cargar_partida():
    try:
        with open("partida.txt", "r") as archivo:
            lineas = archivo.readlines()

        nombre = lineas[0].strip()
        oro = int(lineas[1].strip())
        cantidad_unidades = int(lineas[2].strip())

        reino = Reino(nombre, oro)

        for i in range(3, 3 + cantidad_unidades):
            datos = lineas[i].strip().split("|")

            nombre_unidad = datos[0]
            tropas = int(datos[1])
            potencia = int(datos[2])

            unidad = Unidad(nombre_unidad, tropas, potencia)
            reino.ejercito.append(unidad)

        print("Partida cargada correctamente.")
        return reino

    except FileNotFoundError:
        print("No existe ninguna partida guardada.")
        return None

    except (ValueError, IndexError):
        print("La partida guardada está dañada o tiene datos inválidos.")
        return None


# ==========================================
# MÓDULO 4 — MENÚ PRINCIPAL
# ==========================================

mi_reino = None

while True:
    print("\n================================")
    print("     GRAN ESTRATEGIA PARADOX")
    print("================================")
    print("1. Nueva partida")
    print("2. Cargar partida")
    print("3. Mostrar reino")
    print("4. Reclutar unidad")
    print("5. Atacar")
    print("6. Guardar partida")
    print("7. Salir")
    print("================================")

    opcion = input("Selecciona una opción: ")

    # --------------------------------------
    # NUEVA PARTIDA
    # --------------------------------------

    if opcion == "1":
        nombre = input("Nombre de tu reino: ")

        mi_reino = Reino(nombre, 500)

        print(f"\n¡Has fundado {nombre}!")
        print("Tesoro inicial: 500 de oro.")

    # --------------------------------------
    # CARGAR PARTIDA
    # --------------------------------------

    elif opcion == "2":
        partida = cargar_partida()

        if partida is not None:
            mi_reino = partida

    # --------------------------------------
    # MOSTRAR REINO
    # --------------------------------------

    elif opcion == "3":
        if mi_reino is None:
            print("Primero debes iniciar o cargar una partida.")
        else:
            mi_reino.mostrar_reino()

    # --------------------------------------
    # RECLUTAR UNIDAD
    # --------------------------------------

    elif opcion == "4":
        if mi_reino is None:
            print("Primero debes iniciar o cargar una partida.")
        else:
            print("\n=== RECLUTAMIENTO ===")
            print("1. Caballería Real")
            print("2. Infantería")
            print("3. Arqueros")

            tipo = input("Selecciona una unidad: ")

            if tipo == "1":
                unidad = Unidad("Caballería Real", 100, 10)
                costo = 200

            elif tipo == "2":
                unidad = Unidad("Infantería", 150, 7)
                costo = 150

            elif tipo == "3":
                unidad = Unidad("Arqueros", 80, 8)
                costo = 175

            else:
                print("Tipo de unidad inválido.")
                continue

            mi_reino.reclutar_unidad(unidad, costo)

    # --------------------------------------
    # ATAQUE
    # --------------------------------------

    elif opcion == "5":
        if mi_reino is None:
            print("Primero debes iniciar o cargar una partida.")

        elif len(mi_reino.ejercito) == 0:
            print("No tienes unidades para atacar.")

        else:
            enemigo = Unidad("Ejército enemigo", 100, 5)

            print("\n=== BATALLA ===")

            print("\nTus unidades:")
            for i, unidad in enumerate(mi_reino.ejercito):
                print(f"{i + 1}. {unidad.nombre} - {unidad.tropas} tropas")

            try:
                seleccion = int(input("Selecciona la unidad que atacará: "))

                if seleccion < 1 or seleccion > len(mi_reino.ejercito):
                    print("Unidad inválida.")
                else:
                    unidad_atacante = mi_reino.ejercito[seleccion - 1]
                    unidad_atacante.atacar(enemigo)

                    if enemigo.tropas == 0:
                        print("¡El ejército enemigo ha sido derrotado!")
                    else:
                        print(
                            f"El enemigo conserva {enemigo.tropas} tropas."
                        )

            except ValueError:
                print("Debes introducir un número.")

    # --------------------------------------
    # GUARDAR PARTIDA
    # --------------------------------------

    elif opcion == "6":
        if mi_reino is None:
            print("No hay ninguna partida activa para guardar.")
        else:
            guardar_partida(mi_reino)

    # --------------------------------------
    # SALIR
    # --------------------------------------

    elif opcion == "7":
        print("Campaña finalizada.")
        break

    else:
        print("Opción inválida. Selecciona una opción del 1 al 7.")