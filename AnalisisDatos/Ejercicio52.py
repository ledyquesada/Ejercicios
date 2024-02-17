#Regresion con Bosques

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Cargar conjunto de datos de Boston House Prices
boston = load_boston()
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de Bosques Aleatorios para regresión
rf_model_reg = RandomForestRegressor(random_state=42)
rf_model_reg.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred_reg = rf_model_reg.predict(X_test)

# Evaluar el rendimiento del modelo de regresión
mae = mean_absolute_error(y_test, y_pred_reg)
r2 = r2_score(y_test, y_pred_reg)

print(f'MAE: {mae}')
print(f'R^2 Score: {r2}')
