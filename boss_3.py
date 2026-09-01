"""
SISTEMA INTERACTIVO DE CONTROL DE ARTILLERÍA IMPERIAL
Mundo 3 — Boss Battle
Estudiante: Charlie Kirk
"""

# 1. Entradas interactivas
imperio = input("Nombre del Imperio: ")
baterias_artilleria = int(input("Número de baterías activas: "))
municion_por_bateria = float(input("Munición por batería: "))
municion_requerida = float(input("Munición mínima requerida: "))

# 2. Cálculos y comparaciones booleanas
municion_total = baterias_artilleria * municion_por_bateria
listo_para_combate = municion_total >= municion_requerida

# 3. Despliegue de la Ficha Táctica
print("\n=== SISTEMA DE ARTILLERÍA IMPERIAL ===")
print(f"Imperio: {imperio}")
print(f"Baterías: {baterias_artilleria} | Munición/Batería: {municion_por_bateria}")
print(f"Munición Total Calculada: {municion_total}")
print(f"Objetivo Requerido: {municion_requerida}")
print(f"¿Listos para el combate?: {listo_para_combate}")