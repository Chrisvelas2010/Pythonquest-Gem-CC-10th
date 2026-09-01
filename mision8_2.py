print("=== CARGA DE CAMPAÑA ===")

with open("partida.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())

print("Campaña cargada correctamente.")