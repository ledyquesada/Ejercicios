#SVM vs arboles de decisión

# Importar bibliotecas
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

# Dividir el conjunto de datos
X_train, X_test, y_train, y_test = train_test_split(df_svm_tree[['Feature_1', 'Feature_2']], df_svm_tree['Target'], test_size=0.2, random_state=42)

# SVM
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)
svm_pred = svm_model.predict(X_test)
svm_accuracy = accuracy_score(y_test, svm_pred)

# Árbol de Decisión
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)
tree_pred = tree_model.predict(X_test)
tree_accuracy = accuracy_score(y_test, tree_pred)

# Visualizar las regiones de decisión
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plot_decision_regions(X_train.values, y_train.values, clf=svm_model, legend=2)
plt.title(f'SVM - Precisión: {svm_accuracy:.2f}')

plt.subplot(1, 2, 2)
plot_decision_regions(X_train.values, y_train.values, clf=tree_model, legend=2)
plt.title(f'Árbol de Decisión - Precisión: {tree_accuracy:.2f}')

plt.show()
