print("Bienvenido al supermercado")

#supermercado

opciones = 0
precioLeche = 1.5
precioPan = 0.5
precioHuevos = 0.3
precioCarne = 2.5
precioPescado = 3.5

while opciones != 4:
    print("1. Comprar")
    print("2. Productos")
    print("3. Ofertas")
    print("4. Salir")
    opciones = int(input("Ingrese una opcion: "))

    if opciones == 1:
        print("Comprar")
        diaSemnana = input("Que dia es hoy?")
        nombreCliente = input("Cual es su nombre?")
        producto=input("Selecciona producto=")
        cantidad=int(input("Cantidad="))

        if producto == "leche":
            calcularprecio=precioLeche*cantidad
            print("El precio sera de ", calcularprecio, "€")
        elif producto == "pan":
            calcularprecio=precioPan*cantidad
            print("El precio sera de ", calcularprecio, "€")
        elif producto == "huevos":
            calcularprecio=precioHuevos*cantidad
            print("El precio sera de ", calcularprecio, "€")
        elif producto == "carne":
            calcularprecio=precioCarne*cantidad
            print("El precio sera de ", calcularprecio, "€")
        elif producto == "pescado":
            calcularprecio=precioPescado*cantidad
            print("El precio sera de ", calcularprecio, "€")

    elif opciones == 2:
        ListaProductos = ["leche", "pan", "huevos", "carne", "pescado"]
        print("Lista de productos: ", ListaProductos)

    elif opciones == 3:
        print("Ofertas")

    elif opciones == 4:
        print("Salir")

    else:
        print("incorrecto")