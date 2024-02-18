#Validación Cruzada con Clasificación y Datos Aleatorios

import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Generar datos aleatorios para clasificación binaria
X_clasificacion, y_clasificacion = make_classification(n_samples=200, n_features=2, n_informative=2, n_redundant=0, random_state=42)

# Crear un DataFrame con los datos
datos_clasificacion = pd.DataFrame({'feature1': X_clasificacion[:, 0], 'feature2': X_clasificacion[:, 1], 'y': y_clasificacion})

# Guardar el conjunto de datos en un archivo CSV
datos_clasificacion.to_csv('datos_clasificacion.csv', index=False)

# Separar variables predictoras (X) y variable de clase (y)
X_clasif = datos_clasificacion[['feature1', 'feature2']]
y_clasif = datos_clasificacion['y']

# Crear un clasificador de Bosques Aleatorios
clasif_rf = RandomForestClassifier()

# Realizar validación cruzada estratificada (por ejemplo, k=5)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores_clasificacion = cross_val_score(clasif_rf, X_clasif, y_clasif, cv=skf, scoring='accuracy')

# Imprimir los resultados de la validación cruzada
print("Resultados de la Validación Cruzada (Clasificación):")
for i, score in enumerate(scores_clasificacion, 1):
    print(f"Fold {i}: Accuracy = {score}")

# Imprimir la precisión promedio
print(f"Accuracy Promedio: {scores_clasificacion.mean()}")
