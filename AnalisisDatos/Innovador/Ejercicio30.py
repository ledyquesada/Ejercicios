#Ajuste fino

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Crear un conjunto de datos simulados para clasificación multiclase
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_classes=3, random_state=42)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo de red neuronal
model = Sequential()
model.add(Dense(64, input_dim=20, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo inicial
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

# Realizar ajuste fino desbloqueando las últimas capas
for layer in model.layers[:-1]:
    layer.trainable = False

# Compilar el modelo para ajuste fino
model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Ajuste fino en el nuevo conjunto de datos
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))
