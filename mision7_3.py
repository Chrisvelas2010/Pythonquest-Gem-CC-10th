def calcular_dano_critico(dano_base, multiplicador):
    dano_total = dano_base * multiplicador
    return dano_total


dano = calcular_dano_critico(25, 2)
print(f"Daño crítico: {dano}")  