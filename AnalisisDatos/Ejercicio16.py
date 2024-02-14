#Fechas y seires temporales

import pandas as pd
# a) Agregar la columna 'Dia_Semana'
df_ventas['Dia_Semana'] = df_ventas['Fecha'].dt.day_name()

# b) Filtrar para incluir solo los jueves
df_jueves = df_ventas[df_ventas['Dia_Semana'] == 'Thursday']
