#Graficos interactivos

#instalar libreria
pip install plotly


import seaborn as sns
import plotly.express as px
import pandas as pd

# Crear un DataFrame de ejemplo
np.random.seed(42)
df_ejercicio12 = pd.DataFrame({
    'categoria': np.random.choice(['A', 'B', 'C'], size=100),
    'valor': np.random.randn(100)
})

# Solución con Plotly (debe tener Plotly instalado: pip install plotly)
fig = px.bar(df_ejercicio12, x='categoria', y='valor', color='categoria', barmode='group')
fig.update_layout(title='Gráfico Interactivo de Barras', xaxis_title='Categoría', yaxis_title='Valor')
fig.show()
