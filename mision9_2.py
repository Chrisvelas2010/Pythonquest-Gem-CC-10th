class Gobernante:
    def __init__(self, nombre, reino, oro):
        self.nombre = nombre
        self.reino = reino
        self.oro = oro


mi_gobernante = Gobernante("Carlos", "Castilla", 850)

print("Nombre:", mi_gobernante.nombre)
print("Reino:", mi_gobernante.reino)
print("Oro:", mi_gobernante.oro)