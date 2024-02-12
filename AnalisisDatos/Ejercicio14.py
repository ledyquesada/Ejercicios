#Proporciones

import numpy as np
from scipy.stats import proportions_ztest

# Generar dos conjuntos de datos binarios
data1 = np.random.choice([0, 1], size=100, p=[0.8, 0.2])
data2 = np.random.choice([0, 1], size=120, p=[0.75, 0.25])

# Realizar prueba de hipótesis para proporciones
count1 = np.sum(data1)
count2 = np.sum(data2)
nobs1 = len(data1)
nobs2 = len(data2)

stat, p_value = proportions_ztest([count1, count2], [nobs1, nobs2])

# Imprimir resultados
print(f"Estadística de prueba z: {stat}")
print(f"Valor p: {p_value}")

# Tomar decisión basada en el valor p y nivel de significancia
alpha = 0.05
if p_value < alpha:
    print("Se rechaza la hipótesis nula")
else:
    print("No se rechaza la hipótesis nula")
