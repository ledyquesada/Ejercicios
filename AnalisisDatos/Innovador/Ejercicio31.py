#SVM

from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_classification

# Crear un conjunto de datos simulados para clasificación binaria
X, y = make_classification(n_samples=1000, n_features=15, n_informative=10, n_classes=2, random_state=42)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el clasificador SVM
svm_classifier = SVC()

# Definir la cuadrícula de parámetros a explorar
param_grid = {'C': [0.1, 1, 10],
              'kernel': ['linear', 'rbf', 'poly']}

# Realizar la búsqueda en cuadrícula
grid_search_svm = GridSearchCV(svm_classifier, param_grid, cv=3, scoring='accuracy')
grid_search_svm.fit(X_train, y_train)

# Obtener los mejores parámetros y la precisión asociada
best_params_svm = grid_search_svm.best_params_
best_accuracy_svm = grid_search_svm.best_score_

# Imprimir resultados
print(f"Mejores Parámetros para SVM: {best_params_svm}")
print(f"Precisión en Validación para SVM: {best_accuracy_svm}")
