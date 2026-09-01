nombre_escuadron = input("Nombre del escuadrón: ")
puntos_victoria = int(input("Puntos de victoria: "))

if puntos_victoria >= 1000:
    bono = puntos_victoria * 0.20
    total = puntos_victoria + bono
    print("Escuadrón:", nombre_escuadron)
    print("Total con bono:", total)
else:
    print("El escuadrón no alcanzó el bono de victoria.")