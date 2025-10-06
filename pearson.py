import numpy as np
from scipy.stats import pearsonr

# Datos de ejemplo: horas de estudio vs calificación
horas_estudio = [2, 4, 6, 8, 10]
calificaciones = [60, 70, 80, 85, 95]

# Calcular correlación de Pearson
r, p_value = pearsonr(horas_estudio, calificaciones)

print(f"Coeficiente de Pearson: {r:.3f}")
print(f"Valor p: {p_value:.3f}")

# Interpretación
if r > 0.7:
    print("Correlación positiva fuerte")
elif r > 0.3:
    print("Correlación positiva moderada")
else:
    print("Correlación débil o nula")
