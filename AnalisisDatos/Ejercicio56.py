#Bosques aleatorios

# Importar bibliotecas
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Dividir el conjunto de datos
X_train, X_test, y_train, y_test = train_test_split(df_rf_regression[['Feature']], df_rf_regression['Target'], test_size=0.2, random_state=42)

# Bosques Aleatorios
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_mse = mean_squared_error(y_test, rf_pred)

# Visualizar resultados
plt.scatter(X_test, y_test, color='black', label='Datos reales')
plt.plot(X_test, rf_pred, color='blue', linewidth=3, label=f'Bosques Aleatorios - MSE: {rf_mse:.2f}')
plt.legend()
plt.show()
