#Ejercicio 1

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("datos_conversion.csv")

# Convertir la columna "Fecha" en formato datetime
df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce", dayfirst=True)

# Mostrar los primeros registros para verificar la conversión
print(df.head())


#ejercicio 2
import pandas as pd
import numpy as np

# Cargar el archivo CSV
df = pd.read_csv("datos_conversion.csv")

# Convertir "Ventas" a valores numéricos, manejando errores
df["Ventas"] = pd.to_numeric(df["Ventas"], errors="coerce")

# Convertir "Precio Unitario" a valores numéricos, manejando errores
df["Precio Unitario"] = pd.to_numeric(df["Precio Unitario"], errors="coerce")

# Mostrar las primeras filas
print(df.head())



#Ejercicio 3

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("datos_conversion.csv")

# Generar estadísticas descriptivas del DataFrame
print(df.describe())

# Verificar si quedan valores nulos después de la conversión
print(df.isnull().sum())




#Ejercicio 4

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("datos_conversion.csv")

# Reemplazar valores nulos en "Ventas" con el promedio
df["Ventas"].fillna(df["Ventas"].mean(), inplace=True)

# Reemplazar valores nulos en "Precio Unitario" con 0
df["Precio Unitario"].fillna(0, inplace=True)

# Verificar si quedan valores nulos
print(df.isnull().sum())




