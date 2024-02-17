#Areas apiladas

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Crear un DataFrame de ejemplo
np.random.seed(42)
df = pd.DataFrame({
    'fecha': pd.date_range(start='2022-01-01', periods=50, freq='D'),
    'valor': np.random.randn(50),
    'categoria': np.random.choice(['A', 'B'], size=50)
})

# Solución
sns.lineplot(x='fecha', y='valor', hue='categoria', data=df, ci=None, palette='Paired')
plt.fill_between(df['fecha'], df['valor'], color='skyblue', alpha=0.2)
plt.title('Gráfico de Áreas Apiladas')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.show()
