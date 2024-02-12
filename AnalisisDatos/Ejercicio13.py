# Intervalo de confianza

import numpy as np
from scipy.stats import t

# Generar datos aleatorios
data = np.random.normal(loc=60, scale=10, size=50)

# Calcular el intervalo de confianza para la media (95%)
confidence_level = 0.95
mean_value = np.mean(data)
std_dev = np.std(data)
margin_of_error = t.ppf((1 + confidence_level) / 2, len(data) - 1) * (std_dev / np.sqrt(len(data)))

# Calcular el intervalo de confianza
confidence_interval = (mean_value - margin_of_error, mean_value + margin_of_error)

# Imprimir resultados
print(f"Media: {mean_value}")
print(f"Intervalo de Confianza (95%): {confidence_interval}")
