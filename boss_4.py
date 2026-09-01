"""
BOSS FINAL — MUNDO 4
Sistema de evaluación del estado del imperio.
"""

nombre_imperio = input("Nombre del imperio: ")
tropas = int(input("Cantidad de tropas: "))
defensas = int(input("Nivel de defensas: "))

if tropas >= 500 and defensas >= 300:
    print("Estado de la Nación: IMPERIO INVENTIBLE")
elif tropas >= 300 or defensas >= 150:
    print("Estado de la Nación: IMPERIO ESTABLE")
else:
    print("Estado de la Nación: IMPERIO EN RIESGO")