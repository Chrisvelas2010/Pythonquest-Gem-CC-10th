class Division:
    def __init__(self, nombre, tropas, potencia):
        self.nombre = nombre
        self.tropas = tropas
        self.potencia = potencia

    def mostrar_ficha(self):
        print("=== DIVISIÓN ===")
        print("Nombre:", self.nombre)
        print("Tropas:", self.tropas)
        print("Potencia:", self.potencia)

    def reforzar(self, cantidad):
        self.tropas += cantidad
        print(self.nombre, "ha recibido", cantidad, "tropas de refuerzo.")


division_norte = Division("División Norte", 10000, 85)
division_sur = Division("División Sur", 7500, 70)

division_norte.mostrar_ficha()
division_sur.mostrar_ficha()

division_norte.reforzar(2000)

print("\nDespués de los refuerzos:")
division_norte.mostrar_ficha()
division_sur.mostrar_ficha()

if division_norte.potencia > division_sur.potencia:
    print("\nLa División Norte tiene mayor potencia militar.")
elif division_sur.potencia > division_norte.potencia:
    print("\nLa División Sur tiene mayor potencia militar.")
else:
    print("\nAmbas divisiones tienen la misma potencia.")