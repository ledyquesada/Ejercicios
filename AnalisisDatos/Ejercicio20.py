#Operaciones con ventas

import pandas as pd
import numpy as np

fechas_ventas_temporales = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
ventas_temporales = np.random.randint(50, 200, size=len(fechas_ventas_temporales))

df_ventas_temporales = pd.DataFrame({'Fecha': fechas_ventas_temporales, 'Ventas': ventas_temporales})


# a) Agregar la columna 'Mes'
df_ventas_temporales['Mes'] = df_ventas_temporales['Fecha'].dt.month

# b) Calcular el promedio de ventas para cada mes
promedio_ventas_mes = df_ventas_temporales.groupby('Mes')['Ventas'].mean()
