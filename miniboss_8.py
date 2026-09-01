nombre = input("Introduce el nombre de tu gobernante: ")

try:
    puntos = int(input("Introduce los puntos de la campaña: "))

    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"Gobernante: {nombre} | Puntos: {puntos}\n")

    print("Registro guardado correctamente en puntuaciones.txt")

except ValueError:
    print("Error: los puntos deben ser un número.")