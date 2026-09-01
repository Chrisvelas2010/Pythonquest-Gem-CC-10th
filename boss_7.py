inventario = ["Espada", "Poción"]
oro = 100

tienda = [
    {"nombre": "Escudo", "precio": 40},
    {"nombre": "Arco", "precio": 50},
    {"nombre": "Poción", "precio": 20}
]


def mostrar_menu():
    print("\n===== TIENDA RPG =====")
    print("1. Comprar")
    print("2. Ver inventario")
    print("3. Ver oro")
    print("4. Salir")


def realizar_compra():
    global oro

    print("\n--- OBJETOS DISPONIBLES ---")

    for i, articulo in enumerate(tienda):
        print(f"{i + 1}. {articulo['nombre']} - {articulo['precio']} oro")

    opcion = input("Selecciona un objeto: ")

    if opcion.isdigit():
        indice = int(opcion) - 1

        if 0 <= indice < len(tienda):
            articulo = tienda[indice]

            if oro >= articulo["precio"]:
                oro -= articulo["precio"]
                inventario.append(articulo["nombre"])

                print(f"Has comprado: {articulo['nombre']}")
                print(f"Oro restante: {oro}")
            else:
                print("No tienes suficiente oro.")
        else:
            print("Objeto inválido.")
    else:
        print("Debes introducir un número.")


def mostrar_inventario():
    print("\n--- INVENTARIO ---")

    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        for objeto in inventario:
            print(f"- {objeto}")


while True:
    mostrar_menu()

    opcion = input("Elige una opción: ")

    if opcion == "1":
        realizar_compra()

    elif opcion == "2":
        mostrar_inventario()

    elif opcion == "3":
        print(f"Oro disponible: {oro}")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")