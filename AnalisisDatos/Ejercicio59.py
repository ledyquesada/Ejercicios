# Validacion cruzada con regresión

import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generar datos aleatorios para regresión
X, y = make_regression(n_samples=100, n_features=1, noise=5, random_state=42)

# Crear un DataFrame con los datos
datos_regresion = pd.DataFrame({'X': X.flatten(), 'y': y})

# Guardar el conjunto de datos en un archivo CSV
datos_regresion.to_csv('datos_regresion.csv', index=False)

# Separar variables predictoras (X) y variable objetivo (y)
X_regresion = datos_regresion[['X']]
y_regresion = datos_regresion['y']

# Crear un modelo de regresión lineal
modelo_regresion = LinearRegression()

# Realizar validación cruzada k-fold (por ejemplo, k=3)
scores_regresion = cross_val_score(modelo_regresion, X_regresion, y_regresion, cv=3, scoring='r2')

# Imprimir los resultados de la validación cruzada
print("Resultados de la Validación Cruzada (Regresión Lineal):")
for i, score in enumerate(scores_regresion, 1):
    print(f"Fold {i}: R2 Score = {score}")

# Imprimir el R2 promedio
print(f"R2 Promedio: {scores_regresion.mean()}")
