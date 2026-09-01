class Gobernante:
    def __init__(self, nombre, reino, oro):
        self.nombre = nombre
        self.reino = reino
        self.oro = oro

    def mostrar_ficha(self):
        print("=== FICHA DEL GOBERNANTE ===")
        print("Nombre:", self.nombre)
        print("Reino:", self.reino)
        print("Oro:", self.oro)

    def recaudar_impuestos(self, cantidad):
        self.oro += cantidad
        print("Se han recaudado", cantidad, "de oro.")


gobernante = Gobernante("Carlos", "Castilla", 850)

gobernante.mostrar_ficha()

gobernante.recaudar_impuestos(300)

gobernante.mostrar_ficha()