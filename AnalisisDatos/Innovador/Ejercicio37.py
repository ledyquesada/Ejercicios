#Clasificacion de imagenes

# Implementación del Ejercicio 2

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generar datos aleatorios para clasificación
num_samples = 1000
img_size = (32, 32, 3)  # Imágenes en color
num_classes = 5

X = np.random.rand(num_samples, *img_size)
y = np.random.randint(0, num_classes, size=num_samples)

# Dividir datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocesamiento de datos
X_train = X_train / 255.0  # Normalizar imágenes al rango [0, 1]
X_test = X_test / 255.0

# Convertir etiquetas a one-hot encoding
y_train_one_hot = to_categorical(y_train, num_classes)
y_test_one_hot = to_categorical(y_test, num_classes)

# Definir la arquitectura de la CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=img_size),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(num_classes, activation='softmax')
])

# Compilar y entrenar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train_one_hot, epochs=10, batch_size=32, validation_data=(X_test, y_test_one_hot))

# Evaluar el rendimiento del modelo en el conjunto de prueba
y_pred_one_hot = model.predict(X_test)
y_pred = np.argmax(y_pred_one_hot, axis=1)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on test set: {accuracy}")
