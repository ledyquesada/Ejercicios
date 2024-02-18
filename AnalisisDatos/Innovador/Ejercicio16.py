#Compras en linea

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Crear datos simulados de compras en línea
np.random.seed(42)
data = {
    'product_A': np.random.randint(0, 2, 100),
    'product_B': np.random.randint(0, 2, 100),
    'product_C': np.random.randint(0, 2, 100),
    'category_D': np.random.randint(0, 2, 100),
    'target': np.random.randint(0, 2, 100)
}
df = pd.DataFrame(data)

# Crear nueva característica: proporción de gasto en una categoría específica
category_to_track = 'category_D'
df['spending_ratio'] = df[category_to_track] / df[['product_A', 'product_B', 'product_C']].sum(axis=1)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size=0.2, random_state=42)

# Entrenar un clasificador RandomForest con las nuevas características
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Realizar predicciones y evaluar el rendimiento
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f'Precisión del modelo con nueva característica: {accuracy:.2f}')
