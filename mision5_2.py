recursos = 0
turno = 1

while turno <= 4:
    recolectados = int(input(f"Recursos recolectados en el turno {turno}: "))
    recursos += recolectados

    print(f"Total acumulado: {recursos}")

    turno += 1

print(f"Total de recursos acumulados: {recursos}")