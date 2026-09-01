def calcular_ataque(fuerza):
    return fuerza * 2

#COn vida es la vida dela division
def aplicar_curacion(vida_actual, pocion):
    nueva_vida = vida_actual + pocion

    if nueva_vida > 100:
        nueva_vida = 100

    return nueva_vida


def estado_personaje(nombre, vida):
    print("\n--- ESTADO DEL PERSONAJE ---")
    print(f"Nombre: {nombre}")
    print(f"Vida: {vida}")


nombre = input("Nombre del personaje: ")
fuerza = int(input("Fuerza del personaje: "))
vida = int(input("Vida actual: "))
pocion = int(input("Cantidad de curación de la Div: "))

ataque = calcular_ataque(fuerza)
vida = aplicar_curacion(vida, pocion)

print(f"\nDaño de ataque: {ataque}")

estado_personaje(nombre, vida)