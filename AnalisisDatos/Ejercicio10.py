#Prueba de hipótesis
import numpy as np
from scipy.stats import ttest_ind

# Generar dos conjuntos de datos para la prueba t
group1 = np.random.normal(loc=50, scale=10, size=100)
group2 = np.random.normal(loc=55, scale=10, size=100)

# Realizar prueba t de dos muestras
t_statistic, p_value = ttest_ind(group1, group2)

# Imprimir resultados
print(f"Estadística de prueba t: {t_statistic}")
print(f"Valor p: {p_value}")

# Tomar decisión basada en el valor p y nivel de significancia
alpha = 0.05
if p_value < alpha:
    print("Se rechaza la hipótesis nula")
else:
    print("No se rechaza la hipótesis nula")
