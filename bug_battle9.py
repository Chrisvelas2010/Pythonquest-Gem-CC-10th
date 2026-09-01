class Gobernante:
    def __init__(self, nombre, reino, oro):
        self.nombre = nombre
        self.reino = reino
        self.oro = oro

    def mostrar_ficha(self):
        print("Gobernante:", self.nombre)
        print("Reino:", self.reino)
        print("Oro:", self.oro)

    def recaudar_impuestos(self, cantidad):
        self.oro += cantidad


gobernante = Gobernante("Felipe", "Francia", 500)

gobernante.mostrar_ficha()
gobernante.recaudar_impuestos(200)
gobernante.mostrar_ficha()