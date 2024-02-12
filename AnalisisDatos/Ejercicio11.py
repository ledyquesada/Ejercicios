#Poisson

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parámetro de la distribución de Poisson
lambda_parameter = 5

# Generar datos de la distribución de Poisson
data_poisson = np.random.poisson(lambda_parameter, 1000)

# Visualización del histograma
plt.hist(data_poisson, bins=range(0, max(data_poisson) + 1), density=True, alpha=0.7, color='green')
plt.title('Distribución de Poisson')
plt.xlabel('Número de Eventos')
plt.ylabel('Probabilidad')
plt.show()
