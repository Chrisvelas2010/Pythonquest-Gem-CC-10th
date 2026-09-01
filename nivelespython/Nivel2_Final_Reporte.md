# 🛡️ BITÁCORA DE AVANCE: PYTHON QUEST
**Estudiante:** Charlie Kirk  
**Carpeta de Proyecto:** Pythonquest_Charlie  
**Fecha:** 27 de Agosto de 2026  

---

## 🗺️ Nivel 2: El Poder de los Datos
* **Mundo:** 2 — Variables y Tipos de Datos
* **Estado:** 🏆 COMPLETADO (20%)
* **XP Acumulada:** 245 XP
* **Rango Alcanzado:** 🧭 Explorador Python

---

### 📜 Competencias Desbloqueadas

1. **Variables y Asignación**: Almacenamiento dinámico de datos en memoria.
2. **Tipos de Datos Primarios**:
   * Texto (`str`)
   * Enteros (`int`)
   * Decimales (`float`)
   * Booleanos (`bool`)
3. **Inspección de Tipos (`type()`)**: Identificación en tiempo de ejecución de la clase de dato.
4. **Conversión de Tipos (*Casting*)**: Uso de `int()`, `float()` y `str()` para transformaciones seguras.
5. **Formateo de Cadenas (*f-strings*)**: Intercalación limpia de variables y texto.

---

### 👑 Proyecto Evaluado: `boss_2.py`

```python
"""Descripción Nación"""
nombre_imperio = "Sacrum Imperium Salvadorum"
nivel_tecnologico = 67
pib_trillones = 1.67
en_guerra = False

print(type(en_guerra))

pib_trillones = pib_trillones + pib_trillones * 0.0585

print(f"Natione: {nombre_imperio}\nLvl Tec. : {nivel_tecnologico}\nPIB: {pib_trillones}\nEstado de guerra: {en_guerra}")