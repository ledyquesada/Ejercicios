#Distribuciones multiples

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Crear un DataFrame de ejemplo
np.random.seed(42)
df = pd.DataFrame(np.random.randn(100, 3), columns=['variable1', 'variable2', 'variable3'])

# Solución
sns.kdeplot(data=df[['variable1', 'variable2', 'variable3']], fill=True, common_norm=False, palette='husl')
plt.title('Distribuciones Múltiples')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()
