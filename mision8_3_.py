try:
    tropas = int(input("Introduce el número de tropas de la división: "))
    print(f"La división tiene {tropas} tropas.")

except ValueError:
    print("Error: debes introducir un número entero.")