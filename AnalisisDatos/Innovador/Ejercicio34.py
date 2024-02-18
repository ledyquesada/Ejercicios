#estacionalidad constante

# Generar datos aleatorios con tendencia exponencial y estacionalidad constante
tendencia_exponencial = np.exp(0.02 * np.arange(len(fechas)))
estacionalidad_constante = 3 * np.ones(len(fechas))
datos_3 = tendencia_exponencial + estacionalidad_constante + np.random.normal(0, 1, len(fechas))

# Aplicar el modelo de descomposición
resultado_3 = seasonal_decompose(datos_3, model='additive', period=365)

# Visualizar resultados
plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(fechas, datos_3, label='Datos Observados')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(fechas, resultado_3.trend, label='Tendencia')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(fechas, resultado_3.seasonal, label='Estacionalidad')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(fechas, resultado_3.resid, label='Residuos')
plt.legend()

plt.tight_layout()
plt.show()
