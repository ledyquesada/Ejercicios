#Manipulación avanzada de fechas 

import pandas as pd
import numpy as np

fechas_ventas_diarias = pd.date_range(start='2022-01-01', end='2022-01-31', freq='D')
ventas_diarias = np.random.randint(50, 200, size=len(fechas_ventas_diarias))

df_ventas_diarias = pd.DataFrame({'Fecha': fechas_ventas_diarias, 'Ventas': ventas_diarias})


# a) Agregar la columna 'Dia_Semana'
df_ventas_diarias['Dia_Semana'] = df_ventas_diarias['Fecha'].dt.day_name()

# b) Calcular la suma acumulativa de ventas para cada día de la semana
df_ventas_diarias['Ventas_Acumulativas'] = df_ventas_diarias.groupby('Dia_Semana')['Ventas'].cumsum()
