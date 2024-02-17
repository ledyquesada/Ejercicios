#Datos breast cancer

from sklearn.datasets import load_breast_cancer
import pandas as pd

breast_cancer = load_breast_cancer()
df_breast_cancer = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Aplicar PCA
pca_bc = PCA()
pca_bc.fit(df_breast_cancer)

# Varianza explicada acumulada
varianza_explicada_acum_bc = pca_bc.explained_variance_ratio_.cumsum()

# Determinar número de componentes para explicar al menos el 90% de la varianza
num_componentes_90porc_bc = len(varianza_explicada_acum_bc[varianza_explicada_acum_bc <= 0.90])

print(f"Número de componentes para explicar al menos el 90% de la varianza: {num_componentes_90porc_bc}")

# Graficar la varianza explicada acumulada
plt.plot(range(1, len(varianza_explicada_acum_bc)+1), varianza_explicada_acum_bc, marker='o', linestyle='--')
plt.xlabel('Número de Componentes Principales')
plt.ylabel('Porcentaje Acumulado de Varianza Explicada')
plt.title('Análisis de Varianza Acumulada - Breast Cancer')
plt.show()
