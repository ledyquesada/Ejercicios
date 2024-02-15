#Combinación de Dataframes

import pandas as pd

datos_productos = {'Producto': ['A', 'B', 'C'], 'Precio_Unitario': [10, 20, 30]}
df_productos = pd.DataFrame(datos_productos)

datos_ventas_productos = {'Producto': ['A', 'B', 'C'], 'Cantidad': [50, 30, 40]}
df_ventas_productos = pd.DataFrame(datos_ventas_productos)

# a) Combinar DataFrames para obtener información completa
df_ventas_completas = pd.merge(df_ventas_productos, df_productos, on='Producto', how='left')

# b) Calcular el monto total de ventas para cada producto
df_ventas_completas['Monto_Total'] = df_ventas_completas['Cantidad'] * df_ventas_completas['Precio_Unitario']
