#PCA en Digits

from sklearn.datasets import load_digits
import pandas as pd

digits = load_digits()
df_digits = pd.DataFrame(digits.data, columns=[f'Pixel_{i}' for i in range(1, 65)])


from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Aplicar PCA
pca_digits = PCA(n_components=2)
df_digits_transformado = pd.DataFrame(pca_digits.fit_transform(df_digits), columns=['Componente_1', 'Componente_2'])

# Visualizar dispersión en espacio bidimensional
plt.scatter(df_digits_transformado['Componente_1'], df_digits_transformado['Componente_2'], c=digits.target, cmap='viridis', alpha=0.8)
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('Dispersión en Espacio Bidimensional - Digits')
plt.show()
