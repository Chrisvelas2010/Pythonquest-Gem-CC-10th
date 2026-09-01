inventario = ["espada", "escudo", "poción"]

nuevo_objeto = input("Objeto que deseas agregar: ")
inventario.append(nuevo_objeto)

print("Inventario actualizado:", inventario)

objeto_desechar = input("Objeto que deseas desechar: ")

if objeto_desechar in inventario:
    inventario.remove(objeto_desechar)
    print("Inventario actualizado:", inventario)
else:
    print("Ese objeto no está en el inventario.")