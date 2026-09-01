try:
    archivo = open("partida.txt", "r")

except FileNotFoundError:
    print("No existe ninguna partida guardada.")

else:
    print("=== ESTADO DE LA CAMPAÑA ===")

    for linea in archivo:
        print(linea.strip())

finally:
    print("Proceso de carga finalizado.")