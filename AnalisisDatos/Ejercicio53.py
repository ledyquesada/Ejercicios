#Clasificacion con redes neuronales

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Cargar conjunto de datos Breast Cancer
breast_cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(breast_cancer.data, breast_cancer.target, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de Red Neuronal para clasificación
nn_model = MLPClassifier(random_state=42)
nn_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred_nn = nn_model.predict(X_test)

# Evaluar el rendimiento del modelo de clasificación
accuracy_nn = accuracy_score(y_test, y_pred_nn)
precision_nn = precision_score(y_test, y_pred_nn, average='weighted')
recall_nn = recall_score(y_test, y_pred_nn, average='weighted')
f1_nn = f1_score(y_test, y_pred_nn, average='weighted')

print(f'Accuracy: {accuracy_nn}')
print(f'Precision: {precision_nn}')
print(f'Recall: {recall_nn}')
print(f'F1-Score: {f1_nn}')
