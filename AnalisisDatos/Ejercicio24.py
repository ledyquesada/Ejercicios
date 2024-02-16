#Funcion cuadratica

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = x**2

plt.plot(x, y, label='$y = x^2$')
plt.title('Gráfico de $y = x^2$')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
