#Examen final
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Simulación de datos
np.random.seed(42)
n = 300
data = {
    'Edad': np.random.randint(18, 65, size=n),
    'FrecuenciaCompra': np.random.randint(1, 10, size=n),
    'GastoTotal': np.round(np.random.normal(800000, 200000, size=n), -3),
    'Ciudad': np.random.choice(['Bogotá', 'Tunja', 'Soacha', 'Chía'], size=n),
    'Servicio': np.random.choice(['Internet', 'Móvil', 'TV'], size=n)
}
df = pd.DataFrame(data)

# 2. Crear variable objetivo
df['NivelCliente'] = pd.cut(df['GastoTotal'],
                            bins=[0, 599999, 999999, np.inf],
                            labels=['Bajo', 'Medio', 'Alto'])

# 3. Separar X e y
X = df.drop(columns='NivelCliente')
y = df['NivelCliente']

# 4. Preprocesamiento
categoricas = ['Ciudad', 'Servicio']
numericas = ['Edad', 'FrecuenciaCompra', 'GastoTotal']

preprocesador = ColumnTransformer([
    ('cat', OneHotEncoder(drop='first'), categoricas)
], remainder='passthrough')

# 5. Modelo y pipeline
modelo = Pipeline([
    ('prep', preprocesador),
    ('clf', RandomForestClassifier(random_state=42))
])

# 6. División de datos y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
modelo.fit(X_train, y_train)

# 7. Predicción y evaluación
y_pred = modelo.predict(X_test)
print("📋 Clasification Report:")
print(classification_report(y_test, y_pred))

# 8. Matriz de confusión
cm = confusion_matrix(y_test, y_pred, labels=['Bajo', 'Medio', 'Alto'])
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens',
            xticklabels=['Bajo', 'Medio', 'Alto'],
            yticklabels=['Bajo', 'Medio', 'Alto'])
plt.title("Matriz de Confusión - NivelCliente")
plt.xlabel("Predicho")
plt.ylabel("Real")
plt.show()
