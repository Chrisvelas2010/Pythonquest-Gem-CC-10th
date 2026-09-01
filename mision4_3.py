tropas = int(input("Cantidad de tropas: "))
suministros = int(input("Cantidad de suministros: "))

if tropas >= 100 and suministros >= 50:
    print("¡Despliegue militar aprobado!")
else:
    print("Despliegue cancelado: Faltan tropas o suministros.")