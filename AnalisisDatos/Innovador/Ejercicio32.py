#Tendencia lineal

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Generar datos aleatorios con tendencia y estacionalidad
np.random.seed(42)
fechas = pd.date_range(start='2022-01-01', end='2023-12-31', freq='D')
tendencia_lineal = 0.1 * np.arange(len(fechas))
estacionalidad_sinusoidal = 5 * np.sin(2 * np.pi * (fechas.dayofyear) / 365)
datos = tendencia_lineal + estacionalidad_sinusoidal + np.random.normal(0, 2, len(fechas))

# Aplicar el modelo de descomposición
resultado = seasonal_decompose(datos, model='additive', period=365)

# Visualizar resultados
plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(fechas, datos, label='Datos Observados')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(fechas, resultado.trend, label='Tendencia')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(fechas, resultado.seasonal, label='Estacionalidad')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(fechas, resultado.resid, label='Residuos')
plt.legend()

plt.tight_layout()
plt.show()
