class PersonajeRPG:
    def __init__(self, nombre, vida, fuerza, oro, inventario):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.oro = oro
        self.inventario = inventario

    def atacar(self, enemigo):
        enemigo.recibir_dano(self.fuerza)
        print(self.nombre, "ha atacado a", enemigo.nombre)

    def recibir_dano(self, cantidad):
        self.vida -= cantidad

        if self.vida < 0:
            self.vida = 0

        print(self.nombre, "ha recibido", cantidad, "de daño.")

    def curarse(self, cantidad):
        self.vida += cantidad
        print(self.nombre, "ha recuperado", cantidad, "de vida.")

    def mostrar_estadisticas(self):
        print("\n=== ESTADÍSTICAS ===")
        print("Nombre:", self.nombre)
        print("Vida:", self.vida)
        print("Fuerza:", self.fuerza)
        print("Oro:", self.oro)
        print("Inventario:", self.inventario)


jugador = PersonajeRPG(
    "Rey Alfonso",
    100,
    25,
    500,
    ["Espada", "Escudo", "Poción"]
)

enemigo = PersonajeRPG(
    "Duque enemigo",
    80,
    20,
    300,
    ["Hacha"]
)


while True:
    print("\n=== GRAN CAMPAÑA ===")
    print("1. Atacar")
    print("2. Curarse")
    print("3. Ver estadísticas")
    print("4. Ver estadísticas del enemigo")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        jugador.atacar(enemigo)

        if enemigo.vida == 0:
            print("¡El enemigo ha sido derrotado!")
            break

    elif opcion == "2":
        jugador.curarse(20)

    elif opcion == "3":
        jugador.mostrar_estadisticas()

    elif opcion == "4":
        enemigo.mostrar_estadisticas()

    elif opcion == "5":
        print("Campaña finalizada.")
        break

    else:
        print("Opción inválida.")