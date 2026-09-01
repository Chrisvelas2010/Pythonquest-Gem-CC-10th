coordenadas = (10, 20)

personaje = {
    "nombre": "Charlie",
    "nivel": 5,
    "vida": 100,
    "fuerza": 25
}

print("Coordenadas:", coordenadas)
print("Vida:", personaje["vida"])

personaje["vida"] = 120
personaje["nivel"] += 1

print("Personaje actualizado:", personaje)