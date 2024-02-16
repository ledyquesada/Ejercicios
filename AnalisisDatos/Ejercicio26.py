#Ventas aleatorias

import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
sales = np.random.randint(50, 200, size=12)

plt.bar(months, sales, color='skyblue')
plt.title('Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.show()
