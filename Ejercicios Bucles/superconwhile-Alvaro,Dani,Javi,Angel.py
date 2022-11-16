#Ejercicio hecho entre Dani,Javi,Angel y Alvaro
#No funciona lo del domingo, por eso no esta el if diaSemana!="domingo"...
#Corregir lo de que no te vuelva a preguntar el dia y el nombre a la hora de comprar otro producto 
#supermercado
opciones = 0


diaSemana = 0
nombreCliente=""


#Entrada de datos
precioTotal=0
print("Bienvenido al supermercado.")
print("Nuestras opciones son:")
while opciones != 4:
    print("1. Comprar")
    print("2. Ver Productos")
    print("3. Ver Ofertas")
    print("4. Salir")
    opciones = int(input("Ingrese una opcion: "))
    
    if opciones == 1:

        print("Comprar")
        diaSemana = input("¿Que dia es hoy? ")
        nombreCliente = input("¿Cual es su nombre? ")
        producto=input("Selecciona producto: ")
        cantidadProducto=int(input("Cantidad: "))
   #precios
        if (producto == "leche"):
            precioProducto = 1.5
        elif (producto == "pan"):
            precioProducto = 0.5
        elif (producto == "huevos"):
            precioProducto =  0.3
        elif (producto == "carne"):
            precioProducto = 2.5
        elif (producto == "pescado"):
            precioProducto = 3.5
        else:
            print("El producto no existe")

    #descuentos por dia
        if (diaSemana == "lunes"):
            if (producto == "leche"):
                descuento = 0.8             
        elif (diaSemana == "martes"):
                descuento = 1.2
        elif (diaSemana == "miercoles"):
            if (producto == "pan"):
                descuento = precioProducto
                cantidadProducto = cantidadProducto // 2 + cantidadProducto % 2
        elif (diaSemana == "viernes"):
                descuento = 0.3
        

  #clientes
        if (nombreCliente == "carlos") or (nombreCliente == "ines"):
                if (producto=="leche") or (producto=="pan") or (producto=="huevos"):
                    descuento -= 0.1
        elif (nombreCliente == "SrMuro"):
                    descuento = 1.5
        precioTotal += precioProducto*cantidadProducto*descuento
        print('El precio total es {0:.2f}'.format(precioTotal))

    elif opciones == 2:
        ListaProductos = ["leche", "pan", "huevos", "carne", "pescado"]
        print("Lista de productos: ", ListaProductos)
    
    elif opciones == 3:
        print("Ofertas")
        print("Lunes=>Leche tiene un 20% de descuento")
        print("Martes=>Dia de los bordelines la factura sube un 20%")
        print("Miercoles=>Hay 2x1 en huevos")
        print("Viernes=>70% de descuento en todo")

    elif opciones == 4:
       print("Adios mostro")

    else:
        print("Y si pones el número bien friki")
        
        
  