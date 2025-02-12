#Ejercicio 1:
df_subset = df[["Producto", "Ventas", "Total"]]
print(df_subset.head(7))


#Ejercicio 2:

df_subconjunto = df.loc[:14, ["Fecha", "Precio Unitario"]]
print(df_subconjunto)


#Ejercicio 3

df["Fecha"] = pd.to_datetime(df["Fecha"])

df_filtro = df[(df["Producto"] == "Laptop") & (df["Fecha"] >= "2023-01-10") & (df["Fecha"] <= "2023-01-20")]
df_filtro = df_filtro.sort_values(by="Total", ascending=False)

print(df_filtro)


#Ejercicio 4

precio_promedio = df["Precio Unitario"].mean()
df_filtro = df[(df["Precio Unitario"] > precio_promedio) & (df["Ventas"] > 40)]
df_filtro = df_filtro[["Producto", "Ventas", "Precio Unitario", "Total"]]

print(df_filtro)

