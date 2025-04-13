#SESION 4
#EJERCICIO 1
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

# Cargar el dataset
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Definir la grilla de búsqueda
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [3, 5, None]
}

# Crear el objeto de búsqueda
grid = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid.fit(X_train, y_train)

# Resultados
print("Mejores hiperparámetros:", grid.best_params_)
print("Precisión promedio CV:", grid.best_score_)

#ejercicio 2

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
import numpy as np

# Definir espacio aleatorio de hiperparámetros
param_dist = {
    'n_estimators': randint(50, 150),
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 4, 5]
}

# Random Search
random_search = RandomizedSearchCV(
    GradientBoostingClassifier(),
    param_distributions=param_dist,
    n_iter=5,
    cv=3,
    random_state=42
)
random_search.fit(X_train, y_train)

print("Mejores hiperparámetros:", random_search.best_params_)
print("Precisión promedio CV:", random_search.best_score_)


#ejercicio 3

def optimizar_modelo(modelo, espacio_parametros, X, y):
    busqueda = GridSearchCV(modelo, espacio_parametros, cv=3)
    busqueda.fit(X, y)
    return busqueda.best_estimator_, busqueda.best_score_

# Usar la función con RandomForest
mejor_modelo, mejor_score = optimizar_modelo(
    RandomForestClassifier(),
    {'n_estimators': [50, 100], 'max_depth': [3, 5, None]},
    X_train,
    y_train
)

print("Modelo óptimo:", mejor_modelo)
print("Puntaje CV:", mejor_score)


#SESION 5
#EJERCICIO 1

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# Cargar datos
df = pd.read_csv("/mnt/data/regresion_ridge_lasso.csv")
X = df.drop(columns='target')
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Modelos
modelos = [
    ('Lineal', LinearRegression()),
    ('Ridge', Ridge(alpha=1)),
    ('Lasso', Lasso(alpha=0.1))
]

# Evaluación
for nombre, modelo in modelos:
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    print(f"Modelo: {nombre}")
    print("  MSE:", mean_squared_error(y_test, y_pred))
    print("  R² :", r2_score(y_test, y_pred), '\n')


#EJERCICIO 2

import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso

alphas = [0.01, 0.1, 1, 10]
coefs = []

for a in alphas:
    modelo = Lasso(alpha=a)
    modelo.fit(X_train, y_train)
    coefs.append(modelo.coef_)

# Gráfico
plt.figure(figsize=(8,5))
for i, coef in enumerate(coefs):
    plt.plot(coef, label=f"alpha={alphas[i]}")
plt.axhline(0, color='gray', linestyle='--')
plt.xlabel("Coeficientes")
plt.ylabel("Valor")
plt.legend()
plt.title("Impacto de alpha en coeficientes (Lasso)")
plt.show()


#EJERCICIO 3

from sklearn.linear_model import RidgeCV, LassoCV

# RidgeCV
ridge_cv = RidgeCV(alphas=[0.01, 0.1, 1, 10]).fit(X_train, y_train)
print("Ridge - mejor alpha:", ridge_cv.alpha_)
print("R² test:", ridge_cv.score(X_test, y_test))

# LassoCV
lasso_cv = LassoCV(alphas=[0.01, 0.1, 1, 10]).fit(X_train, y_train)
print("\nLasso - mejor alpha:", lasso_cv.alpha_)
print("R² test:", lasso_cv.score(X_test, y_test))


#SESION 6
#EJERCICIO 1

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Cargar datos
df = pd.read_csv("/mnt/data/desbalanceado.csv")
X = df.drop(columns='target')
y = df['target']

# División
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Modelo
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Evaluación
y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred))


#EJERCICIO 2

from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

# Oversampling
ros = RandomOverSampler(random_state=42)
X_ros, y_ros = ros.fit_resample(X_train, y_train)

modelo.fit(X_ros, y_ros)
print("Con Oversampling:")
print(classification_report(y_test, modelo.predict(X_test)))

# Undersampling
rus = RandomUnderSampler(random_state=42)
X_rus, y_rus = rus.fit_resample(X_train, y_train)

modelo.fit(X_rus, y_rus)
print("Con Undersampling:")
print(classification_report(y_test, modelo.predict(X_test)))

#SESION 7
#EJERCICIO 1

from imblearn.over_sampling import SMOTE

# SMOTE
sm = SMOTE(random_state=42)
X_sm, y_sm = sm.fit_resample(X_train, y_train)

modelo.fit(X_sm, y_sm)
print("Con SMOTE:")
print(classification_report(y_test, modelo.predict(X_test)))


#EJERCICIO 2

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Paso 1: Cargar datos
df = pd.read_csv("/mnt/data/overfitting_data.csv")
X = df.drop(columns='target')
y = df['target']

# División
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Paso 2: Modelo sobreajustado (sin restricciones)
modelo_overfit = DecisionTreeClassifier(random_state=42)
modelo_overfit.fit(X_train, y_train)

print("🔴 Modelo sin restricciones")
print("Train:", modelo_overfit.score(X_train, y_train))
print("Test :", modelo_overfit.score(X_test, y_test))

# Paso 4: Corrección del sobreajuste con hiperparámetros
modelo_podado = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    max_leaf_nodes=15,
    random_state=42
)
modelo_podado.fit(X_train, y_train)

print("\n🟢 Modelo podado")
print("Train:", modelo_podado.score(X_train, y_train))
print("Test :", modelo_podado.score(X_test, y_test))

# Paso 5: Comparación más detallada
print("\n🔍 Comparación detallada:")
print("Reporte clasificación - Árbol sin restricciones")
print(classification_report(y_test, modelo_overfit.predict(X_test)))

print("\nReporte clasificación - Árbol podado")
print(classification_report(y_test, modelo_podado.predict(X_test)))


