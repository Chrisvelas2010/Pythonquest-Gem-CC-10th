inventario = ["espada", "escudo", "poción"]

while True:
    print("\n--- INVENTARIO ---")
    print("1. Ver inventario")
    print("2. Agregar objeto")
    print("3. Eliminar objeto")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Inventario:", inventario)

    elif opcion == "2":
        objeto = input("Objeto que deseas agregar: ")
        inventario.append(objeto)
        print("Objeto agregado.")

    elif opcion == "3":
        objeto = input("Objeto que deseas eliminar: ")

        if objeto in inventario:
            inventario.remove(objeto)
            print("Objeto eliminado.")
        else:
            print("Ese objeto no está en el inventario.")

    elif opcion == "4":
        print("Saliendo del inventario...")
        break

    else:
        print("Opción inválida.")