import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generar datos de una distribución normal
mu, sigma = 0, 1
data_normal = np.random.normal(mu, sigma, 1000)

# Visualización del histograma
plt.hist(data_normal, bins=30, density=True, alpha=0.7, color='blue')

# Añadir la función de densidad de probabilidad
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, sigma)
plt.plot(x, p, 'k', linewidth=2)

plt.title('Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.show()
