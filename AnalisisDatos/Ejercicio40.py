#Visualizacion multidimensional

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Crear un DataFrame de ejemplo
np.random.seed(42)
df = pd.DataFrame({
    'variable1': np.random.randn(100),
    'variable2': np.random.randn(100),
    'variable3': np.random.randn(100),
    'columna_categorica': np.random.choice(['A', 'B', 'C'], size=100)
})

# Solución
sns.pairplot(df, hue='columna_categorica', palette='husl', markers=['o', 's', 'D'])
plt.suptitle('Pair Plot Multidimensional con Seaborn')
plt.show()
