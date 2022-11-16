#supermercado con while
# Autor: Javier Epifanio López
# Fecha: 10/10/2019
#
# Variables a usar
#   -producto = producto que se va a comprar
#   -precio = precio del producto
#   -cantidad = cantidad de productos que se van a comprar
#   -total = total de la compra
#   -opcion = opción del menú
#   -opciones = lista de opciones del menú
# Algoritmo:
#   -Mostrar menú
#   -Pedir opción
#   -Mientras opción sea distinta de 3
#       -Si opción es 1
#           -Pedir producto
#           -Pedir precio
#           -Pedir cantidad
#           -Calcular total
#       -Si opción es 2
#           -Mostrar total
#       -Si opción es 3
#           -Mostrar mensaje de despedida
#       -Si opción no es 1, 2 o 3
#           -Mostrar mensaje de error


productos = []
opciones = ["1. Añadir producto", "2. Mostrar total", "3. Salir"]
opcion = 0

while opcion != 3:
    for i in range(0, len(opciones)):
        print(opciones[i])
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        producto = input("Ingrese el producto: ")
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
        total = precio * cantidad
        productos.append([producto, precio, cantidad, total])
    elif opcion == 2:
        print("Total: ", sum([i[3] for i in productos]))
    elif opcion == 3:
        print("Adiós")
    else:
        print("Opción no válida")

