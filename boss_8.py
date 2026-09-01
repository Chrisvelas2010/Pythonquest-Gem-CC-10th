while True:
    print("\n=== GRAN CAMPAÑA ===")
    print("1. Nueva Partida")
    print("2. Cargar Partida")
    print("3. Guardar Partida")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del gobernante: ")

        try:
            nivel = int(input("Nivel del gobernante: "))
            oro = int(input("Cantidad de oro: "))

            print("Nueva campaña creada.")

        except ValueError:
            print("Error: nivel y oro deben ser números.")

    elif opcion == "2":
        try:
            with open("partida.txt", "r") as archivo:
                datos = archivo.read()

            print("\n=== PARTIDA CARGADA ===")
            print(datos)

        except FileNotFoundError:
            print("No hay ninguna partida guardada previamente.")

    elif opcion == "3":
        try:
            with open("partida.txt", "w") as archivo:
                archivo.write(f"Nombre: {nombre}\n")
                archivo.write(f"Nivel: {nivel}\n")
                archivo.write(f"Oro: {oro}\n")

            print("Partida guardada correctamente.")

        except NameError:
            print("Primero debes crear una nueva partida.")

    elif opcion == "4":
        print("Campaña finalizada.")
        break

    else:
        print("Opción inválida.")