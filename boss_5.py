vida_jugador = 100
vida_enemigo = 100

while vida_jugador > 0 and vida_enemigo > 0:
    daño = int(input("¿Cuánto daño deseas infligir?: "))

    vida_enemigo -= daño

    if vida_enemigo > 0:
        vida_jugador -= 15

    print(f"Vida del jugador: {vida_jugador}")
    print(f"Vida del enemigo: {vida_enemigo}")
    print()

if vida_enemigo <= 0:
    print("¡Victoria! Has derrotado al enemigo.")
else:
    print("¡Derrota! El enemigo ha vencido.")