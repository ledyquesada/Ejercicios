import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear DataFrame con datos simulados
datos = {
    'cliente': [
        'Ana', 'Luis', 'Sofía', 'Carlos', 'Ana', 'Luis', 'Sofía', 'Ana', 'Carlos', 'Luis'
    ],
    'producto': [
        'Laptop', 'Mouse', 'Monitor', 'Teclado', 'Mouse', 'Monitor', 'Laptop', 'Audífonos', 'Laptop', 'Audífonos'
    ],
    'cantidad': [1, 2, 1, 1, 3, 2, 1, 2, 1, 1],
    'precio_unitario': [1200, 50, 300, 100, 50, 300, 1200, 100, 1200, 100],
    'fecha_pedido': [
        '2024-04-01', '2024-04-02', '2024-04-02', '2024-04-03', '2024-04-04',
        '2024-04-04', '2024-04-05', '2024-04-06', '2024-04-06', '2024-04-07'
    ]
}

df = pd.DataFrame(datos)

# 2. Calcular total por venta
df['total_venta'] = df['cantidad'] * df['precio_unitario']

# 3. Agrupar por cliente
resumen = df.groupby('cliente').agg({
    'total_venta': 'sum',
    'producto': 'count'  # cuenta número de pedidos
}).rename(columns={'producto': 'n_pedidos'})

# 4. Visualizar total gastado por cliente
plt.figure(figsize=(8, 5))
resumen['total_venta'].sort_values().plot(kind='barh', color='skyblue')
plt.title('Total gastado por cliente')
plt.xlabel('Total en $')
plt.ylabel('Cliente')
plt.tight_layout()
plt.show()

# 5. Clasificar clientes por nivel de gasto
resumen['categoria'] = pd.cut(
    resumen['total_venta'],
    bins=[0, 500, 1000, float('inf')],
    labels=['Bajo', 'Medio', 'Alto']
)

# Mostrar resumen final
print("Resumen por cliente:")
print(resumen)

# Opcional: exportar
# resumen.to_csv("resumen_clientes.csv")
