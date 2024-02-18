#Red neuronal con Random

import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from sklearn.datasets import make_regression
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor

# Crear un conjunto de datos simulados para regresión
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Función para crear el modelo de red neuronal
def create_model(learning_rate=0.01, units=64):
    model = Sequential()
    model.add(Dense(units, input_dim=10, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Convertir el modelo en un estimador compatible con scikit-learn
model = KerasRegressor(build_fn=create_model, epochs=10, batch_size=32, verbose=0)

# Definir la distribución de parámetros a explorar
param_dist = {'learning_rate': np.logspace(-4, 0, num=5),
              'units': [32, 64, 128]}

# Realizar la búsqueda aleatoria
random_search = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=10, cv=3, scoring='neg_mean_squared_error')
random_search.fit(X_train, y_train)

# Obtener los mejores parámetros y el error cuadrático medio asociado
best_params = random_search.best_params_
best_mse = -random_search.best_score_

# Imprimir resultados
print(f"Mejores Parámetros: {best_params}")
print(f"Error Cuadrático Medio en Validación: {best_mse}")
