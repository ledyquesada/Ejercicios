#COMPARACION DE MODELOS

# Importar bibliotecas
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Dividir el conjunto de datos
X_train, X_test, y_train, y_test = train_test_split(
    df_model_comparison.drop('Target', axis=1), df_model_comparison['Target'], test_size=0.2, random_state=42
)

# Modelos
svm_model = SVC()
tree_model = DecisionTreeClassifier(random_state=42)
rf_model = RandomForestClassifier(random_state=42)

# Entrenar modelos
svm_model.fit(X_train, y_train)
tree_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)

# Evaluar modelos
svm_report = classification_report(y_test, svm_model.predict(X_test))
tree_report = classification_report(y_test, tree_model.predict(X_test))
rf_report = classification_report(y_test, rf_model.predict(X_test))

print('SVM Report:')
print(svm_report)
print('\nÁrbol de Decisión Report:')
print(tree_report)
print('\nBosques Aleatorios Report:')
print(rf_report)
