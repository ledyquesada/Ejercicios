#Regresión Múltiple

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Generar datos para regresión múltiple
x1 = np.random.rand(100)
x2 = np.random.rand(100)
y = 2 * x1 + 3 * x2 + 1 + np.random.randn(100)  # y = 2x1 + 3x2 + 1 + ruido

# Realizar análisis de regresión múltiple
slope1, intercept1, _, _, _ = linregress(x1, y)
slope2, intercept2, _, _, _ = linregress(x2, y)

# Visualización
plt.scatter(x1, y, label='Datos - x1')
plt.scatter(x2, y, label='Datos - x2')
plt.plot(x1, slope1 * x1 + intercept1, color='red', label='Regresión Lineal x1')
plt.plot(x2, slope2 * x2 + intercept2, color='green', label='Regresión Lineal x2')
plt.title('Análisis de Regresión Múltiple')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
