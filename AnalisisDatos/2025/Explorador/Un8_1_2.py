# Ver productos únicos en el DataFrame
print(df["Producto"].unique())

# Agrupar ventas por categoría y sumarlas
ventas_categoria = df.groupby("Categoría")["Ventas"].sum()

# Ordenar resultados de mayor a menor
print(ventas_categoria.sort_values(ascending=False))
