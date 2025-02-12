#Ejercicio 1
df["Descuento"] = df["Total"] * df["Categoría"].apply(lambda x: 0.10 if x == "Electrónica" else 0.05)
df["Total con Descuento"] = df["Total"] - df["Descuento"]

print(df[["Producto", "Categoría", "Total", "Descuento", "Total con Descuento"]].head())


#Ejercicio 2

df.loc[df["Ventas"] > 50, "Precio Unitario"] = df["Precio Unitario"] * 1.08

print(df[["Producto", "Ventas", "Precio Unitario"]].head())


#Ejercicio 3

df["Margen de Ganancia"] = df["Total"] - (df["Total"] * 0.65)

print(df[["Producto", "Total", "Margen de Ganancia"]].head())


#Ejercicio 4:

df.loc[df["Producto"].isin(["Teclado", "Monitor"]), "Categoría"] = "Periféricos"

print(df[["Producto", "Categoría"]].head(10))
