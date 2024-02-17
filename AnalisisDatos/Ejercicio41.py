#Datos Iris para PCA
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)

from sklearn.decomposition import PCA

# Aplicar PCA
pca_iris = PCA()
pca_iris.fit(df_iris)

# Determinar número de componentes para explicar el 95% de la varianza
num_componentes_95porc_iris = len(pca_iris.explained_variance_ratio_[pca_iris.explained_variance_ratio_.cumsum() <= 0.95])

print(f"Número de componentes para explicar al menos el 95% de la varianza: {num_componentes_95porc_iris}")
