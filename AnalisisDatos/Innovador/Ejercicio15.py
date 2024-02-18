#Dataset de viviendas

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Crear datos simulados de viviendas
np.random.seed(42)
data = {
    'size': np.random.randint(1000, 3000, 100),
    'rooms': np.random.randint(2, 6, 100),
    'location': np.random.choice(['Suburb', 'Urban', 'Rural'], 100),
    'price': np.random.randint(100000, 500000, 100)
}
df = pd.DataFrame(data)

# Crear nueva característica: relación entre tamaño y número de habitaciones
df['size_to_rooms_ratio'] = df['size'] / df['rooms']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df.drop('price', axis=1), df['price'], test_size=0.2, random_state=42)

# Entrenar un modelo de regresión lineal con las nuevas características
model = LinearRegression()
model.fit(X_train[['size', 'rooms', 'size_to_rooms_ratio']], y_train)

# Realizar predicciones y evaluar el rendimiento
X_test['size_to_rooms_ratio'] = X_test['size'] / X_test['rooms']  # Crear la característica en el conjunto de prueba
y_pred = model.predict(X_test[['size', 'rooms', 'size_to_rooms_ratio']])
mse = mean_squared_error(y_test, y_pred)

print(f'MSE del modelo con nueva característica: {mse:.2f}')
