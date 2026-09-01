nivel = int(input("Nivel de experiencia del comandante: "))

if nivel >= 80:
    print("Rango: General Imperial")
elif nivel >= 50:
    print("Rango: Capitán de Frente")
else:
    print("Rango: Recluta de Guardia")