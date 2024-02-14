#Resampling

import pandas as pd

fechas_diario = pd.date_range(start='2022-01-01', end='2022-01-10', freq='D')
datos_diario = [50, 45, 60, 55, 75, 80, 65, 70, 90, 85]

df_diario = pd.DataFrame({'Fecha': fechas_diario, 'Datos': datos_diario})

# a) Resamplear para obtener valores promedio semanales
df_semanal = df_diario.resample('W-Mon', on='Fecha').mean()

# b) Calcular la diferencia en días
diferencia_dias = (df_diario['Fecha'].max() - df_diario['Fecha'].min()).days
