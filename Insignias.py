def filtrar_pares_suma_mayor(lista):
    # Filtrar los números pares de la lista
    numeros_pares = [num for num in lista if num % 2 == 0]

    # Calcular la suma total de los pares
    suma_pares = sum(numeros_pares)

    # Evaluar si la suma es mayor a 50
    if suma_pares > 50:
        return numeros_pares
    else:
        return "Suma insuficiente"

# Ejemplo de prueba
print(filtrar_pares_suma_mayor([10, 15, 20, 25, 30, 35]))  # Salida: [10, 20, 30]
print(filtrar_pares_suma_mayor([2, 4, 6, 8]))  # Salida: "Suma insuficiente"
