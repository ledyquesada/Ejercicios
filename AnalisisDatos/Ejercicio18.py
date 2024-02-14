#Joining de Dataframes

import pandas as pd

datos_clientes = {'ID': [1, 2, 3], 'Nombre': ['Juan', 'Ana', 'Pedro']}
df_clientes = pd.DataFrame(datos_clientes)


datos_compras = {'ID': [1, 2, 4], 'Producto': ['A', 'B', 'C']}
df_compras = pd.DataFrame(datos_compras)


# a) Completar datos faltantes con información de clientes
df_compras_completado = pd.merge(df_compras, df_clientes, on='ID', how='left')

# b) Crear DataFrame con información de compras y fechas de venta
fechas_ventas = pd.date_range(start='2022-01-01', end='2022-01-03', freq='D')
df_ventas = pd.DataFrame({'Fecha': fechas_ventas, 'Producto': ['A', 'B', 'C'], 'ID': [1, 2, 4]})
df_ventas = pd.merge(df_ventas, df_clientes, on='ID', how='left')
