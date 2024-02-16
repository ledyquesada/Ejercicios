#Puntos aleatorios

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.rand(100) * 10 - 5
y = np.random.rand(100) * 10 - 5

quadrant_colors = np.arctan2(y, x)

plt.scatter(x, y, c=quadrant_colors, cmap='hsv', alpha=0.8)
plt.title('Gráfico de Dispersión con Colores por Cuadrante')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Ángulo')
plt.show()
