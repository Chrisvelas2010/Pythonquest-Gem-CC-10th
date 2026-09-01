estadisticas = [35, 72, 48, 90, 61]
total = 0

for elemento in estadisticas:
    if elemento > 50:
        print(f"{elemento}: Superior al límite")
    else:
        print(f"{elemento}: Inferior o igual al límite")

    total += elemento

print(f"Suma total: {total}")