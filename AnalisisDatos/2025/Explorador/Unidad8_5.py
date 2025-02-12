#Ejercicio 1

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("datos_duplicados.csv")

# Contar valores duplicados
print("Total de filas duplicadas:", df.duplicated().sum())

# Mostrar solo las filas duplicadas
print(df[df.duplicated()])


#Ejercicio 2
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("datos_duplicados.csv")

# Número de filas antes de eliminar duplicados
print("Filas antes:", df.shape[0])

# Eliminar duplicados manteniendo la primera aparición
df_sin_duplicados = df.drop_duplicates()

# Número de filas después de eliminar duplicados
print("Filas después:", df_sin_duplicados.shape[0])

#Ejercicio 3

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("datos_duplicados.csv")

# Ordenar por "Precio Unitario" en orden descendente
df_sorted = df.sort_values(by="Precio Unitario", ascending=False)

# Eliminar duplicados manteniendo solo la fila con el mayor "Precio Unitario"
df_filtrado = df_sorted.drop_duplicates(subset=["Producto", "Ventas"], keep="first")

# Mostrar las filas resultantes
print(df_filtrado)


#Ejerecicio 4

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("datos_duplicados.csv")























