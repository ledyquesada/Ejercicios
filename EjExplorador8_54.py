# -*- coding: utf-8 -*-
"""EjExplorador8_54.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UEGKzyk1IH4AvxwWblKDiHSqBKZcCopm
"""

#Multiplo

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 > num2 and num1 % num2 == 0:
    print(f"{num1} es múltiplo de {num2}.")
elif num2 > num1 and num2 % num1 == 0:
    print(f"{num2} es múltiplo de {num1}.")
else:
    print("El mayor no es múltiplo del menor.")