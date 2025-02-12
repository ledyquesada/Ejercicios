#Ejercicio 1

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("datos_groupby.csv")

# Agrupar por categoría y sumar ventas
ventas_categoria = df.groupby("Categoría")["Cantidad Vendida"].sum()

# Crear gráfico de barras
plt.figure(figsize=(8,5))
ventas_categoria.plot(kind="bar", color="skyblue", edgecolor="black")

# Personalización del gráfico
plt.title("Total de Ventas por Categoría", fontsize=14)
plt.xlabel("Categoría", fontsize=12)
plt.ylabel("Cantidad Vendida", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Mostrar gráfico
plt.show()


#Ejercicio 2

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("datos_groupby.csv")

# Convertir la columna "Fecha" en formato datetime
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Agrupar por fecha y sumar ventas
ventas_fecha = df.groupby("Fecha")["Cantidad Vendida"].sum()

# Crear gráfico de líneas
plt.figure(figsize=(10,5))
plt.plot(ventas_fecha.index, ventas_fecha.values, marker="o", linestyle="-", color="blue", linewidth=2)

# Personalización del gráfico
plt.title("Tendencia de Ventas en el Tiempo", fontsize=14)
plt.xlabel("Fecha", fontsize=12)
plt.ylabel("Cantidad Vendida", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis="both", linestyle="--", alpha=0.7)

# Mostrar gráfico
plt.show()



#Ejercicio 3

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("datos_groupby.csv")

# Crear histograma de precios unitarios
plt.figure(figsize=(8,5))
plt.hist(df["Precio Unitario"], bins=10, color="purple", edgecolor="black", alpha=0.7)

# Personalización del gráfico
plt.title("Distribución de Precios de Productos", fontsize=14)
plt.xlabel("Precio Unitario", fontsize=12)
plt.ylabel("Frecuencia", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Mostrar gráfico
plt.show()


#Ejerciio 4

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("datos_groupby.csv")

# Agrupar por producto y sumar ventas
ventas_producto = df.groupby("Producto")["Cantidad Vendida"].sum().sort_values()

# Crear gráfico de barras horizontal
plt.figure(figsize=(8,5))
ventas_producto.plot(kind="barh", color="green", edgecolor="black")

# Personalización del gráfico
plt.title("Ventas Totales por Producto", fontsize=14)
plt.xlabel("Cantidad Vendida", fontsize=12)
plt.ylabel("Producto", fontsize=12)
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Mostrar gráfico
plt.show()

















