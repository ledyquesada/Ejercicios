#Lineas de conexion

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)

plt.scatter(x, y, color='blue')
plt.plot(x, y, linestyle='dashed', color='gray', marker='o')
plt.title('Gráfico de Dispersión con Líneas de Conexión')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
