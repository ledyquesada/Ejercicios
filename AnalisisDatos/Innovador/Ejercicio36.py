#Generacion de imagenes

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, LeakyReLU, BatchNormalization, Reshape, Flatten, Input
from tensorflow.keras.datasets import mnist

# Cargar datos MNIST
(X_train, _), (_, _) = mnist.load_data()
X_train = (X_train.astype(np.float32) - 127.5) / 127.5  # Normalizar imágenes al rango [-1, 1]
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)

# Definir arquitectura de la GAN
latent_dim = 100

# Generador
generator = Sequential([
    Dense(128, input_dim=latent_dim),
    LeakyReLU(alpha=0.2),
    BatchNormalization(),
    Dense(784, activation='tanh'),  # Tangente hiperbólica para escalar a [-1, 1]
    Reshape((28, 28, 1))
])

# Discriminador
discriminator = Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(128),
    LeakyReLU(alpha=0.2),
    Dense(1, activation='sigmoid')
])

# Construir la GAN conectando el generador y el discriminador
discriminator.trainable = False  # Congelar pesos del discriminador durante el entrenamiento del generador

gan_input = Input(shape=(latent_dim,))
x = generator(gan_input)
gan_output = discriminator(x)

gan = Model(gan_input, gan_output)
gan.compile(optimizer='adam', loss='binary_crossentropy')

# Compilar el modelo discriminador
discriminator.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar la GAN
epochs = 10000
batch_size = 64

for epoch in range(epochs):
    noise = np.random.normal(0, 1, size=(batch_size, latent_dim))
    generated_images = generator.predict(noise)

    real_images = X_train[np.random.randint(0, X_train.shape[0], batch_size)]
    labels_real = np.ones((batch_size, 1))
    labels_fake = np.zeros((batch_size, 1))

    d_loss_real = discriminator.train_on_batch(real_images, labels_real)
    d_loss_fake = discriminator.train_on_batch(generated_images, labels_fake)
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

    noise = np.random.normal(0, 1, size=(batch_size, latent_dim))
    labels_gan = np.ones((batch_size, 1))

    g_loss = gan.train_on_batch(noise, labels_gan)

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}/{epochs} [D loss: {d_loss[0]} | D accuracy: {100 * d_loss[1]}] [G loss: {g_loss}]")

# Generar imágenes con el generador entrenado
def generate_images(rows, columns):
    noise = np.random.normal(0, 1, size=(rows * columns, latent_dim))
    generated_images = generator.predict(noise)
    generated_images = 0.5 * generated_images + 0.5  # Desnormalizar imágenes al rango [0, 1]

    fig, axs = plt.subplots(rows, columns, figsize=(10, 10))
    idx = 0
    for i in range(rows):
        for j in range(columns):
            axs[i, j].imshow(generated_images[idx, :, :, 0], cmap='gray')
            axs[i, j].axis('off')
            idx += 1
    plt.show()

# Visualizar imágenes generadas
generate_images(5, 5)
