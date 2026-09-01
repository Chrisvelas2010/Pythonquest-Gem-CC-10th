for numero in range(1, 11):
    if numero == 5:
        continue

    if numero == 8:
        print("¡Alerta! Se ha alcanzado la unidad 8.")
        break

    print(f"Valor actual: {numero}")