#Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que
#seleccionamos la opción de “Salir”.

#datos:
opciones = ["1. Opción 1", "2. Opción 2", "3. Opción 3", "4. Opción 4", "5. Opción 5", "6. Salir"]
opcion = 0

#proceso:
while opcion != 6:
    for i in range(0, len(opciones)):
        print(opciones[i])
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print("Opción 1")
    elif opcion == 2:
        print("Opción 2")
    elif opcion == 3:
        print("Opción 3")
    elif opcion == 4:
        print("Opción 4")
    elif opcion == 5:
        print("Opción 5")
    elif opcion == 6:
        print("Salir")
    else:
        print("Opción no válida")
        