#Tendencia logaritmica

# Generar datos aleatorios con tendencia logarítmica y estacionalidad aleatoria
tendencia_logaritmica = 3 * np.log(np.arange(1, len(fechas) + 1))
estacionalidad_aleatoria = np.random.normal(0, 2, len(fechas))
datos_4 = tendencia_logaritmica + estacionalidad_aleatoria + np.random.normal(0, 2, len(fechas))

# Aplicar el modelo de descomposición
resultado_4 = seasonal_decompose(datos_4, model='additive', period=365)

# Visualizar resultados
plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(fechas, datos_4, label='Datos Observados')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(fechas, resultado_4.trend, label='Tendencia')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(fechas, resultado_4.seasonal, label='Estacionalidad')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(fechas, resultado_4.resid, label='Residuos')
plt.legend()

plt.tight_layout()
plt.show()
