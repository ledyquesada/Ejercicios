import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("ventas_tienda.csv")

# Mostrar las primeras 10 filas
print(df.head(10))

# Mostrar información del DataFrame
print(df.info())

# Verificar valores nulos
print(df.isnull().sum())
