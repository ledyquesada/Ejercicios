#Barras apíladas

import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 6)
category1 = np.random.randint(10, 30, size=5)
category2 = np.random.randint(20, 40, size=5)
category3 = np.random.randint(5, 15, size=5)

plt.bar(months, category1, color='skyblue', label='Categoría 1')
plt.bar(months, category2, bottom=category1, color='lightcoral', label='Categoría 2')
plt.bar(months, category3, bottom=category1 + category2, color='lightgreen', label='Categoría 3')

plt.title('Gráfico de Barras Apiladas')
plt.xlabel('Mes')
plt.ylabel('Valor')
plt.legend()
plt.show()
