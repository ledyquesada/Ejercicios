#diabetes

from sklearn.datasets import load_diabetes
import pandas as pd

diabetes = load_diabetes()
df_diabetes = pd.DataFrame(diabetes.data, columns=[f'Feature_{i}' for i in range(1, 11)])

from sklearn.decomposition import PCA

# Aplicar PCA
pca_diabetes = PCA()
pca_diabetes.fit(df_diabetes)

# Determinar número de componentes para explicar al menos el 99% de la varianza
num_componentes_99porc_diabetes = len(pca_diabetes.explained_variance_ratio_[pca_diabetes.explained_variance_ratio_.cumsum() <= 0.99])

print(f"Número de componentes para explicar al menos el 99% de la varianza: {num_componentes_99porc_diabetes}")
