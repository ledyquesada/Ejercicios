#Ejercicio 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv("datos_comparacion.csv")

# Crear el gráfico de dispersión con línea de tendencia
plt.figure(figsize=(8,5))
sns.regplot(x="Edad", y="Ingreso Mensual", data=df, scatter_kws={"color": "blue"}, line_kws={"color": "red"})

# Personalización del gráfico
plt.title("Relación entre Edad e Ingreso Mensual", fontsize=14)
plt.xlabel("Edad", fontsize=12)
plt.ylabel("Ingreso Mensual", fontsize=12)

# Mostrar gráfico
plt.show()


#Ejercicio 2

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv("datos_comparacion.csv")

# Agrupar por Región y calcular promedio de Gasto Mensual
gasto_region = df.groupby("Región")["Gasto Mensual"].mean()

# Crear gráfico de barras apiladas
plt.figure(figsize=(8,5))
gasto_region.plot(kind="bar", color=["blue", "orange", "green", "red"], edgecolor="black")

# Personalización del gráfico
plt.title("Promedio de Gasto Mensual por Región", fontsize=14)
plt.xlabel("Región", fontsize=12)
plt.ylabel("Gasto Mensual", fontsize=12)
plt.xticks(rotation=45)

# Mostrar gráfico
plt.show()




#Ejercicio 3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv("datos_comparacion.csv")

# Crear histograma doble
plt.figure(figsize=(8,5))
plt.hist(df["Ingreso Mensual"], bins=10, alpha=0.5, label="Ingreso Mensual", color="blue", edgecolor="black")
plt.hist(df["Gasto Mensual"], bins=10, alpha=0.5, label="Gasto Mensual", color="red", edgecolor="black")

# Personalización del gráfico
plt.title("Distribución de Ingreso y Gasto Mensual", fontsize=14)
plt.xlabel("Monto ($)", fontsize=12)
plt.ylabel("Frecuencia", fontsize=12)
plt.legend()

# Mostrar gráfico
plt.show()




#Ejercicio 4

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv("datos_comparacion.csv")

# Crear figura
plt.figure(figsize=(8,5))

# Crear boxplot
sns.boxplot(x="Puntuación de Crédito", y="Ingreso Mensual", data=df, color="lightblue")

# Superponer swarmplot
sns.swarmplot(x="Puntuación de Crédito", y="Ingreso Mensual", data=df, color="red", alpha=0.6)

# Personalización del gráfico
plt.title("Distribución del Ingreso según Puntuación de Crédito", fontsize=14)
plt.xlabel("Puntuación de Crédito", fontsize=12)
plt.ylabel("Ingreso Mensual", fontsize=12)

# Mostrar gráfico
plt.show()




#Ejercicio 5

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv("datos_comparacion.csv")

# Crear subconjuntos por grupo de edad
jovenes = df[df["Edad"] <= 30]["Ingreso Mensual"]
adultos = df[(df["Edad"] > 30) & (df["Edad"] <= 50)]["Ingreso Mensual"]
mayores = df[df["Edad"] > 50]["Ingreso Mensual"]

# Crear KDE Plot
plt.figure(figsize=(8,5))
sns.kdeplot(jovenes, label="Jóvenes (18-30)", shade=True, color="blue")
sns.kdeplot(adultos, label="Adultos (31-50)", shade=True, color="green")
sns.kdeplot(mayores, label="Mayores (51-65)", shade=True, color="red")

# Personalización del gráfico
plt.title("Distribución del Ingreso Mensual por Grupo de Edad", fontsize=14)
plt.xlabel("Ingreso Mensual", fontsize=12)
plt.ylabel("Densidad", fontsize=12)
plt.legend()

# Mostrar gráfico
plt.show()

