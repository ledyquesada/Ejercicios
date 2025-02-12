#Ejercicio 1

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("datos_groupby.csv")

# Agrupar por Categoría y sumar las ventas
ventas_por_categoria = df.groupby("Categoría")["Cantidad Vendida"].sum()

# Mostrar resultados
print(ventas_por_categoria)


#Ejercicio 2

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("datos_groupby.csv")

# Agrupar por Categoría y calcular el precio promedio
precio_promedio_categoria = df.groupby("Categoría")["Precio Unitario"].mean()

# Mostrar resultados
print(precio_promedio_categoria)

#Ejercicio 3

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("datos_groupby.csv")

# Contar el número de ventas por Producto
ventas_por_producto = df.groupby("Producto")["Venta_ID"].count()

# Mostrar resultados
print(ventas_por_producto)



#Ejercicio 4

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("datos_groupby.csv")

# Calcular estadísticas de la cantidad vendida por categoría
estadisticas_ventas = df.groupby("Categoría")["Cantidad Vendida"].agg(["min", "max", "mean", "std"])

# Mostrar resultados
print(estadisticas_ventas)




