# Crear columna de ingresos
df["Ingresos"] = df["Ventas"] * df["Precio Unitario"]

# Filtrar productos con ingresos mayores a 5000
df_filtrado = df[df["Ingresos"] > 5000]

# Mostrar las primeras 5 filas
print(df_filtrado.head())
