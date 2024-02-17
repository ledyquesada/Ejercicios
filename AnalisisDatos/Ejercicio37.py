#Tendencias temporales

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Crear una serie temporal de ejemplo
np.random.seed(42)
date_rng = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
serie_temporal = pd.Series(np.random.randn(len(date_rng)), index=date_rng)

# Solución
sns.lineplot(x=serie_temporal.index, y=serie_temporal.values, ci=None, color='purple')
plt.title('Análisis de Tendencias Temporales')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.show()
