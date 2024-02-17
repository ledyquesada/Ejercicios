#Datos Boston

from sklearn.datasets import load_boston
import pandas as pd

boston = load_boston()
df_boston = pd.DataFrame(boston.data, columns=boston.feature_names)


from sklearn.decomposition import PCA

# Aplicar PCA
pca_boston = PCA(n_components=2)
df_boston_transformado = pd.DataFrame(pca_boston.fit_transform(df_boston), columns=['Componente_1', 'Componente_2'])

# Interpretar significado de los primeros dos componentes principales
interpretacion_componentes = pd.DataFrame(pca_boston.components_, columns=df_boston.columns, index=['Componente_1', 'Componente_2'])

print("Interpretación de los componentes principales:")
print(interpretacion_componentes)
