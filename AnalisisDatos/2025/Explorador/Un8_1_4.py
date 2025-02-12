# Convertir la columna "Fecha" en formato datetime
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Filtrar ventas entre el 5 y 20 de enero de 2023
ventas_periodo = df[(df["Fecha"] >= "2023-01-05") & (df["Fecha"] <= "2023-01-20")]

# Mostrar el número total de ventas en el período
print(ventas_periodo["Ventas"].sum())
