#Box Plot avanzado

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Crear un DataFrame de ejemplo
np.random.seed(42)
df = pd.DataFrame({
    'columna_categorica': np.random.choice(['A', 'B', 'C'], size=100),
    'columna_numerica': np.random.randn(100)
})

# Solución
sns.boxplot(x='columna_categorica', y='columna_numerica', data=df, showfliers=False, meanline=True, meanprops={'color': 'red'})
plt.title('Box Plot Avanzado por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.show()
