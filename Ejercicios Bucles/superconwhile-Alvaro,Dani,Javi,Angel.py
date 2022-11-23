#Ejercicio hecho entre Dani,Javi,Angel y Alvaro
#No funciona lo del domingo, por eso no esta el if diaSemana!="domingo"...
#Corregir lo de que no te vuelva a preguntar el dia y el nombre a la hora de comprar otro producto 
#supermercado
opciones = 0
precioLeche=1.5
precioPan=0.5
precioHuevo=0.3
precioCarne=2.5
precioPescado=3.5

diaSemana = 0
nombreCliente=""
comprar=True



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
        print("Comprar:")
        diaSemana = input("¿Que dia es hoy? ")
        nombreCliente = input("¿Cual es su nombre? ")
        producto=input("Selecciona producto: ")
        cantidadProducto=int(input("Cantidad: "))
        
   #precios
        if (producto == "leche"):
            precioProducto = precioLeche
        elif (producto == "pan"):
            precioProducto = precioPan
        elif (producto == "huevos"):
            precioProducto =  precioHuevo
        elif (producto == "carne"):
            precioProducto = precioCarne
        elif (producto == "pescado"):
            precioProducto = precioPescado
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
                cantidadProducto = cantidadProducto // 2 + cantidadProducto % 2
        elif (diaSemana == "viernes"):
                descuento = 0.3
        else:
            descuento = 1


  #clientes
        if nombreCliente =='carlos' or nombreCliente =='ines' and producto=='leche':
                descuento -= 0.1
        elif (nombreCliente == "SrMuro"):
                    descuento = 1.5
        elif (nombreCliente == "carlos" or nombreCliente == "ines" and producto == "pan"):
                    descuento = 0.5
        while comprar==True:
            precioTotal=(precioProducto*cantidadProducto*descuento)
            pregunta=input("¿Desea seguir comprando producto? (si/no) ")
            if pregunta=="si":
                producto=input("Selecciona producto: ")
                cantidadProducto=int(input("Cantidad: "))
                    
            elif pregunta=="no":
                precioTotal+=precioTotal
                print("Gracias por su compra, su precio total es {0:.2f}".format(precioTotal), "€")
                exit()
        

    elif opciones == 2:
        ListaProductos = ["leche", "pan", "huevos", "carne", "pescado"]
        print("Nuestros productos: ", ListaProductos)

    elif opciones == 3:
        print("Ofertas:")
        print("Lunes=>Leche tiene un 20% de descuento")
        print("Martes=>Dia de los bordelines la factura sube un 20%")
        print("Miercoles=>Hay 2x1 en huevos")
        print("Viernes=>70% de descuento en todo")

    elif opciones == 4:
        print("Adios, esperamos verle pronto")

    else:
        print("Ingrese una opcion valida")
        
        
  