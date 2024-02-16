#Histograma

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30, color='lightblue', edgecolor='black')
plt.title('Histograma de Datos Normales')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()
