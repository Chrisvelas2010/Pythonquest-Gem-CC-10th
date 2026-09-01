oro_global = 100


def comprar_item(precio):
    saldo_restante = oro_global - precio
    return saldo_restante


oro_global = comprar_item(35)

print(f"Oro restante: {oro_global}")