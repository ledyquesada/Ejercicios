#Ejercicio 1

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("ventas_tienda.csv")

# Contar valores nulos por columna
print(df.isnull().sum())

# Mostrar solo las filas con valores nulos
print(df[df.isnull().any(axis=1)])

#Ejercicio 2

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("ventas_tienda.csv")

# Número de filas antes de la eliminación
print("Filas antes:", df.shape[0])

# Eliminar filas con valores nulos
df_limpio = df.dropna()

# Número de filas después de la eliminación
print("Filas después:", df_limpio.shape[0])


#Ejercicio 3

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("ventas_tienda.csv")

# Calcular la media de la columna "Ventas"
media_ventas = df["Ventas"].mean()

# Reemplazar valores nulos con la media
df["Ventas"].fillna(media_ventas, inplace=True)

# Verificar si quedan valores nulos
print(df.isnull().sum())


#Ejrcicio 4

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("ventas_tienda.csv")

# Reemplazar valores nulos en la columna "Categoría"
df["Categoría"].fillna("Desconocido", inplace=True)

# Verificar que no haya valores nulos en la columna
print(df["Categoría"].isnull().sum())


#Ejercicio 5

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("ventas_tienda.csv")

# Reemplazar valores nulos en "Precio Unitario" con el promedio de su categoría
df["Precio Unitario"] = df.groupby("Categoría")["Precio Unitario"].transform(lambda x: x.fillna(x.mean()))

# Verificar que no haya valores nulos
print(df.isnull().sum())














