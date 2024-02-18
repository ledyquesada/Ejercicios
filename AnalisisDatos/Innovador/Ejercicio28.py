# Parametros con Grid Search

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Crear un conjunto de datos simulados
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_classes=2, random_state=42)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo de Regresión Logística
model = LogisticRegression()

# Definir la cuadrícula de parámetros a explorar
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100]}

# Realizar la búsqueda en cuadrícula
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Obtener los mejores parámetros y la precisión asociada
best_params = grid_search.best_params_
best_accuracy = grid_search.best_score_

# Imprimir resultados
print(f"Mejores Parámetros: {best_params}")
print(f"Precisión en Validación: {best_accuracy}")
