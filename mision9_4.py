class Gobernante:
    def __init__(self, nombre, reino, oro):
        self.nombre = nombre
        self.reino = reino
        self.oro = oro

    def gastar_oro(self, cantidad):
        if self.oro >= cantidad:
            self.oro -= cantidad
            print("Se han gastado", cantidad, "de oro.")
        else:
            print("No tienes suficiente oro para realizar este gasto.")


gobernante = Gobernante("Carlos", "Castilla", 1000)

print("Oro inicial:", gobernante.oro)

gobernante.gastar_oro(300)
print("Oro restante:", gobernante.oro)

gobernante.gastar_oro(900)
print("Oro restante:", gobernante.oro)