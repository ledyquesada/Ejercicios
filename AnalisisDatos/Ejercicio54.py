#Regresion con redes neuronales

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Cargar conjunto de datos Diabetes
diabetes = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de Red Neuronal para regresión
nn_model_reg = MLPRegressor(random_state=42)
nn_model_reg.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred_reg_nn = nn_model_reg.predict(X_test)

# Evaluar el rendimiento del modelo de regresión
mae_nn = mean_absolute_error(y_test, y_pred_reg_nn)
r2_nn = r2_score(y_test, y_pred_reg_nn)

print(f'MAE: {mae_nn}')
print(f'R^2 Score: {r2_nn}')
