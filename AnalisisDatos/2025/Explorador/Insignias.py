import pandas as pd

# Crear DataFrame con los datos proporcionados
data = {
    "ID": [1,2,3,4,5,6,7,8,9,10],
    "Producto": ["Laptop", "Monitor", "Teclado", "Laptop", "Tablet", "Impresora", "Smartphone", "Mouse", "Monitor", "Tablet"],
    "Categoría": ["Electrónica", "Computación", "Accesorios", "Electrónica", "Computación", "Oficina", "Electrónica", "Accesorios", "Computación", "Computación"],
    "Ventas": [15, 8, 25, 10, 20, 5, 30, 40, 12, 18],
    "Precio Unitario": [1200, 500, 50, 1100, 700, 400, 800, 20, 450, 750],
    "Total Ventas": [18000, 4000, 1250, 11000, 14000, 2000, 24000, 800, 5400, 13500],
    "Región": ["Norte", "Sur", "Norte", "Este", "Oeste", "Norte", "Sur", "Este", "Oeste", "Norte"]
}

df = pd.DataFrame(data)

# 1. Cantidad total de productos vendidos
print(df["Ventas"].sum())

# 2. Categoría con mayor total de ventas acumuladas
print(df.groupby("Categoría")["Total Ventas"].sum().idxmax())

# 3. Productos con precio unitario mayor a 500
print(df[df["Precio Unitario"] > 500])

# 4. Precio promedio de todos los productos
print(df["Precio Unitario"].mean())

# 5. Nueva columna con aumento del 10% en los precios
df["Precio Actualizado"] = df["Precio Unitario"] * 1.10
print(df[["Producto", "Precio Unitario", "Precio Actualizado"]])
