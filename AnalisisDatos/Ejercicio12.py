#Exponencial

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Parámetro de la distribución exponencial (tasa de ocurrencia)
lambda_parameter_exp = 0.5

# Generar datos de la distribución exponencial
data_exponential = np.random.exponential(scale=1/lambda_parameter_exp, size=1000)

# Visualización del histograma
plt.hist(data_exponential, bins=30, density=True, alpha=0.7, color='orange')
plt.title('Distribución Exponencial')
plt.xlabel('Tiempo hasta el Evento')
plt.ylabel('Densidad de Probabilidad')
plt.show()
