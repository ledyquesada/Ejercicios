#Tendencia cuadratica

# Generar datos aleatorios con tendencia cuadrática y estacionalidad exponencial
tendencia_cuadratica = 0.02 * np.arange(len(fechas))**2
estacionalidad_exponencial = 2**((fechas.dayofyear) / 365)
datos_2 = tendencia_cuadratica + estacionalidad_exponencial + np.random.normal(0, 5, len(fechas))

# Aplicar el modelo de descomposición
resultado_2 = seasonal_decompose(datos_2, model='multiplicative', period=365)

# Visualizar resultados
plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(fechas, datos_2, label='Datos Observados')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(fechas, resultado_2.trend, label='Tendencia')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(fechas, resultado_2.seasonal, label='Estacionalidad')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(fechas, resultado_2.resid, label='Residuos')
plt.legend()

plt.tight_layout()
plt.show()
