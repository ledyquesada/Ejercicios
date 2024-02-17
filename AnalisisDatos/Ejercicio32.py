
#Distribuciones

import seaborn as sns
import matplotlib.pyplot as plt

# Solución
sns.set(style="whitegrid")
sns.histplot(data=df['columna'], kde=True, color='skyblue')
plt.title('Histograma y KDE')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()
