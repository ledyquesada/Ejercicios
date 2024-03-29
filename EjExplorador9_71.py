# -*- coding: utf-8 -*-
"""EjExplorador9_71.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZeXjPTR_v4qMvoIgyd7cZt_wdUuntcCG
"""

#Base de datos de Clientes

def gestionar_base_de_datos():
    base_de_datos = {}

    while True:
        print("\nMenú:")
        print("1. Añadir cliente")
        print("2. Eliminar cliente")
        print("3. Mostrar cliente")
        print("4. Listar todos los clientes")
        print("5. Listar clientes preferenciales")
        print("6. Terminar")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            nit = input("Ingrese el NIT del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            correo = input("Ingrese el correo del cliente: ")
            preferencial = input("¿Es cliente preferencial? (Sí/No): ").lower() == 'si'

            datos_cliente = {'nombre': nombre, 'dirección': direccion, 'teléfono': telefono, 'correo': correo, 'preferencial': preferencial}
            base_de_datos[nit] = datos_cliente
            print("Cliente añadido correctamente.")

        elif opcion == '2':
            nit_eliminar = input("Ingrese el NIT del cliente a eliminar: ")
            if nit_eliminar in base_de_datos:
                del base_de_datos[nit_eliminar]
                print("Cliente eliminado correctamente.")
            else:
                print("No se encontró un cliente con ese NIT.")

        elif opcion == '3':
            nit_mostrar = input("Ingrese el NIT del cliente a mostrar: ")
            if nit_mostrar in base_de_datos:
                print("Datos del cliente:")
                print(base_de_datos[nit_mostrar])
            else:
                print("No se encontró un cliente con ese NIT.")

        elif opcion == '4':
            print("Lista de todos los clientes:")
            for nit, datos_cliente in base_de_datos.items():
                print(f"NIT: {nit}, Nombre: {datos_cliente['nombre']}")

        elif opcion == '5':
            print("Lista de clientes preferenciales:")
            for nit, datos_cliente in base_de_datos.items():
                if datos_cliente['preferencial']:
                    print(f"NIT: {nit}, Nombre: {datos_cliente['nombre']}")

        elif opcion == '6':
            print("Programa terminado.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    gestionar_base_de_datos()