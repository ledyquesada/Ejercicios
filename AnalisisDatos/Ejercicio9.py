#Correlación y Regresión

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, linregress

# Generar datos para correlación y regresión
x = np.random.rand(100)
y = 2 * x + 1 + np.random.randn(100)  # y = 2x + 1 + ruido

# Calcular correlación
correlation_coefficient, _ = pearsonr(x, y)

# Calcular regresión lineal
slope, intercept, _, _, _ = linregress(x, y)

# Visualización
plt.scatter(x, y, label='Datos')
plt.plot(x, slope * x + intercept, color='red', label='Regresión Lineal')
plt.title('Correlación y Regresión Lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

print(f"Coeficiente de Correlación: {correlation_coefficient}")
