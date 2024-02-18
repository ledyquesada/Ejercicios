#Hiperparámetros en Ridge y LASSO

# Importar bibliotecas
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error
import numpy as np

# Definir conjunto de datos
X = df_ridge_lasso[['Feature_1', 'Feature_2', 'Feature_3']]
y = df_ridge_lasso['Target']

# Parámetros a sintonizar
alphas = np.logspace(-6, 6, 13)

# Ridge
ridge_params = {'alpha': alphas}
ridge_grid = GridSearchCV(Ridge(), ridge_params, cv=5)
ridge_grid.fit(X, y)
ridge_best_alpha = ridge_grid.best_params_['alpha']
ridge_model = Ridge(alpha=ridge_best_alpha)
ridge_model.fit(X, y)
ridge_pred = ridge_model.predict(X)
ridge_mse = mean_squared_error(y, ridge_pred)

# LASSO
lasso_params = {'alpha': alphas}
lasso_grid = GridSearchCV(Lasso(), lasso_params, cv=5)
lasso_grid.fit(X, y)
lasso_best_alpha = lasso_grid.best_params_['alpha']
lasso_model = Lasso(alpha=lasso_best_alpha)
lasso_model.fit(X, y)
lasso_pred = lasso_model.predict(X)
lasso_mse = mean_squared_error(y, lasso_pred)

print(f'Ridge - Mejor Alpha: {ridge_best_alpha:.2e}, MSE: {ridge_mse:.2f}')
print(f'LASSO - Mejor Alpha: {lasso_best_alpha:.2e}, MSE: {lasso_mse:.2f}')
