#Función bidimensional

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.linspace(0, 2 * np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

plt.contour(X, Y, Z, cmap='viridis')
plt.title('Gráfico de Contorno para $z = \sin(x) + \cos(y)$')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Z')
plt.show()
