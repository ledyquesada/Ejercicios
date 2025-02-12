#Ejercicio 1

import pandas as pd

# Cargar los archivos CSV
df_productos = pd.read_csv("productos.csv")
df_ventas = pd.read_csv("ventas1.csv")

# Realizar la fusión (inner join) por "Producto_ID"
df_merged = df_ventas.merge(df_productos, on="Producto_ID", how="inner")

# Mostrar las primeras filas del nuevo DataFrame fusionado
print(df_merged.head())

#Ejercicio 2

import pandas as pd

# Cargar los archivos CSV
df_productos = pd.read_csv("productos.csv")
df_ventas = pd.read_csv("ventas1.csv")

# Realizar la fusión (left join) para mantener todas las ventas
df_merged_left = df_ventas.merge(df_productos, on="Producto_ID", how="left")

# Mostrar las primeras filas del DataFrame resultante
print(df_merged_left.head())




#Ejerecicio 3

import pandas as pd

# Cargar los archivos CSV
df_productos = pd.read_csv("productos.csv")
df_ventas = pd.read_csv("ventas1.csv")

# Realizar la fusión (right join) para mantener todos los productos
df_merged_right = df_ventas.merge(df_productos, on="Producto_ID", how="right")

# Mostrar las primeras filas del DataFrame resultante
print(df_merged_right.head())





#Ejercicio 4

import pandas as pd

# Cargar los archivos CSV
df_productos = pd.read_csv("productos.csv")
df_ventas = pd.read_csv("ventas1.csv")

# Establecer "Producto_ID" como índice en ambos DataFrames
df_productos.set_index("Producto_ID", inplace=True)
df_ventas.set_index("Producto_ID", inplace=True)

# Realizar la fusión usando .join()
df_joined = df_ventas.join(df_productos, how="inner")

# Mostrar las primeras filas del DataFrame resultante
print(df_joined.head())

#Ejercicio 5

import pandas as pd

# Cargar los archivos CSV
df_productos = pd.read_csv("productos.csv")
df_ventas = pd.read_csv("ventas1.csv")

# Restaurar índices y fusionar los DataFrames
df_productos.reset_index(inplace=True)
df_ventas.reset_index(inplace=True)
df_final = df_ventas.merge(df_productos, on="Producto_ID", how="inner")

# Crear la columna de Ingresos Totales
df_final["Ingresos Totales"] = df_final["Cantidad Vendida"] * df_final["Precio Unitario"]

# Mostrar las primeras filas del DataFrame resultante
print(df_final[["Producto", "Cantidad Vendida", "Precio Unitario", "Ingresos Totales"]].head())











