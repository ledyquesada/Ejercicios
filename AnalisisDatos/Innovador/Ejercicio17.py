#Ventas mensuales

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Crear datos simulados de ventas mensuales
np.random.seed(42)
date_rng = pd.date_range(start='2022-01-01', end='2022-12-31', freq='M')
data = {
    'date': date_rng,
    'sales': np.random.randint(10000, 50000, len(date_rng))
}
df = pd.DataFrame(data)

# Crear nueva característica: tasa de crecimiento de las ventas
df['sales_growth_rate'] = df['sales'].pct_change()

# Eliminar NaN resultantes de la creación de la nueva característica
df = df.dropna()

# Dividir el conjunto de datos en entrenamiento y prueba
train_size = int(len(df) * 0.8)
train, test = df.iloc[:train_size], df.iloc[train_size:]

# Entrenar un modelo de regresión lineal con las nuevas características
X_train, y_train = train['date'].dt.month.values.reshape(-1, 1), train['sales_growth_rate']
X_test, y_test = test['date'].dt.month.values.reshape(-1, 1), test['sales_growth_rate']

model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones y evaluar el rendimiento
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print(f'R^2 del modelo con nueva característica: {r2:.2f}')
