#Datos wine

from sklearn.datasets import load_wine
import pandas as pd

wine = load_wine()
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Aplicar PCA
pca_wine = PCA(n_components=2)
df_wine_transformado = pd.DataFrame(pca_wine.fit_transform(df_wine), columns=['Componente_1', 'Componente_2'])

# Visualizar dispersión en espacio bidimensional
plt.scatter(df_wine_transformado['Componente_1'], df_wine_transformado['Componente_2'], c=wine.target, cmap='viridis', alpha=0.8)
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('Dispersión en Espacio Bidimensional - Wine')
plt.show()
