#Análisis de datos temporales

import pandas as pd
import numpy as np

fechas_datos_temporales = pd.date_range(start='2022-01-01', end='2022-12-31', freq='M')
datos_temporales = np.random.randint(1, 100, size=len(fechas_datos_temporales))

df_datos_temporales = pd.DataFrame({'Fecha': fechas_datos_temporales, 'Datos': datos_temporales})


fechas_ventas_mensuales = pd.date_range(start='2022-01-01', end='2022-12-31', freq='M')
ventas_mensuales = np.random.randint(5000, 10000, size=len(fechas_ventas_mensuales))

serie_ventas_mensuales = pd.Series(ventas_mensuales, index=fechas_ventas_mensuales)

# a) Agregar la columna 'Ventas' al DataFrame
df_datos_temporales['Ventas'] = df_datos_temporales['Fecha'].map(serie_ventas_mensuales)

# b) Calcular el promedio para cada trimestre del año
df_datos_temporales['Trimestre'] = df_datos_temporales['Fecha'].dt.to_period('Q')
promedio_trimestral = df_datos_temporales.groupby('Trimestre')[['Datos', 'Ventas']].mean()
