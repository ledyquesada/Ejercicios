#Operaciones con arrays

import pandas as pd

datos_puntuaciones = {'Nombre': ['Juan', 'Ana', 'Pedro'], 'Puntuacion': [8, 9, 7]}
df_puntuaciones = pd.DataFrame(datos_puntuaciones)

# a) Añadir 1 punto a cada puntuación
df_puntuaciones['Puntuacion'] += 1

# b) Calcular el promedio de las puntuaciones
promedio_puntuaciones = df_puntuaciones['Puntuacion'].mean()
