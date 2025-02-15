#Ejercicio 1

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("datos_groupby.csv")

# Crear boxplot de precios por categoría
plt.figure(figsize=(8,5))
sns.boxplot(x="Categoría", y="Precio Unitario", data=df, palette="Set2")

# Personalización del gráfico
plt.title("Distribución de Precios por Categoría", fontsize=14)
plt.xlabel("Categoría", fontsize=12)
plt.ylabel("Precio Unitario", fontsize=12)
plt.xticks(rotation=45)

# Mostrar gráfico
plt.show()


#Ejercicio 2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("datos_groupby.csv")

# Calcular la matriz de correlación
correlation_matrix = df.corr()

# Crear heatmap de correlación
plt.figure(figsize=(8,5))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f")

# Personalización del gráfico
plt.title("Matriz de Correlación", fontsize=14)

# Mostrar gráfico
plt.show()


#Ejercicio 3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("datos_groupby.csv")

# Crear boxplot de cantidad vendida por producto
plt.figure(figsize=(10,6))
sns.boxplot(x="Producto", y="Cantidad Vendida", data=df, palette="muted")

# Personalización del gráfico
plt.title("Distribución de Ventas por Producto", fontsize=14)
plt.xlabel("Producto", fontsize=12)
plt.ylabel("Cantidad Vendida", fontsize=12)
plt.xticks(rotation=45)

# Mostrar gráfico
plt.show()


#Ejercicio 4

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("datos_groupby.csv")

# Crear tabla pivote para el heatmap
ventas_pivot = df.pivot_table(index="Producto", columns="Categoría", values="Cantidad Vendida", aggfunc="sum")

# Crear heatmap de ventas por categoría y producto
plt.figure(figsize=(8,6))
sns.heatmap(ventas_pivot, annot=True, cmap="Blues", linewidths=0.5)

# Personalización del gráfico
plt.title("Ventas por Categoría y Producto", fontsize=14)
plt.xlabel("Categoría", fontsize=12)
plt.ylabel("Producto", fontsize=12)

# Mostrar gráfico
plt.show()


