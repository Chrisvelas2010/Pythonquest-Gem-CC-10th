tienda = [
    {"nombre": "Espada", "precio": 50},
    {"nombre": "Escudo", "precio": 40},
    {"nombre": "Poción", "precio": 20},
    {"nombre": "Arco", "precio": 60}
]

oro = 100
inventario_jugador = []

while True:
    print("\n--- TIENDA ---")

    for i, articulo in enumerate(tienda):
        print(f"{i}. {articulo['nombre']} - {articulo['precio']} oro")

    print("Escribe 'salir' para terminar.")

    seleccion = input("¿Qué artículo deseas comprar?: ")

    if seleccion.lower() == "salir":
        break

    if seleccion.isdigit():
        indice = int(seleccion)

        if 0 <= indice < len(tienda):
            articulo = tienda[indice]

            if oro >= articulo["precio"]:
                oro -= articulo["precio"]
                inventario_jugador.append(articulo["nombre"])

                print(f"Has comprado {articulo['nombre']}.")
                print(f"Oro restante: {oro}")
            else:
                print("Fondos insuficientes.")
        else:
            print("Índice de artículo inválido.")

    else:
        encontrado = False

        for articulo in tienda:
            if articulo["nombre"].lower() == seleccion.lower():
                encontrado = True

                if oro >= articulo["precio"]:
                    oro -= articulo["precio"]
                    inventario_jugador.append(articulo["nombre"])

                    print(f"Has comprado {articulo['nombre']}.")
                    print(f"Oro restante: {oro}")
                else:
                    print("Fondos insuficientes.")

                break

        if not encontrado:
            print("Artículo no encontrado.")

print("\n--- RESUMEN FINAL ---")
print("Inventario:", inventario_jugador)
print("Oro restante:", oro)