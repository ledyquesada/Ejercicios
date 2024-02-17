#Barras categoricas

import seaborn as sns
import matplotlib.pyplot as plt

# Solución
sns.countplot(x='columna_categorica', data=df, palette='pastel')
plt.title('Count Plot de Categorías')
plt.xlabel('Categoría')
plt.ylabel('Cantidad')
plt.show()
