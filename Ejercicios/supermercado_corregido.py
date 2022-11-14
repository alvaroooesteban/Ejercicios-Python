#Establecer precio de los productos:
precioFruta=3.50
precioCarne=5.80
precioPescado=9.20
precioLeche=6.20
precioPan=0.60

#MENU DE PRODUCTOS
print("Bienvenido al supermercado 2.1, nuestros productos son:")
print("1. Fruta", precioFruta , "€")
print("2. Carne" , precioCarne , "€")
print("3. Pescado" , precioPescado , "€")
print("4. Leche" , precioLeche , "€")
print("5. Pan" , precioPan , "€") 

#Menu de promociones
print("Promociones:")
print("Lunes: 20% de descuento en fruta")
print("Miercoles: 2x1 en pescado")
print("Viernes: 70% de descuento en todos los productos")
print("Domingo: Cerrado")
print("Martes: 20% de subida en la factura")
#Menu de clientes
print("Clientes VIP:")
print("Producto 1, 2 y 3 con un 10% de descuento")
print("Clientes Pufo:")
print("Paga un 50% mas y no tiene descuentos")

#pedir dia de la semana:
diaSemana=input("¿Que dia es hoy? ")

mensaje="Hoy es domingo, el supermercado esta cerrado"

if (diaSemana != "domingo"):
    #quien eres
    nombre = input("¿Como te llamas? ")
    #pedir nombre producto
    nombreProducto = input("¿Que producto quieres comprar? ")
    #pedir cantidad producto
    cantidadProducto = int(input("¿Cuantos productos quieres comprar? "))
    #pedir nombre producto1
    nombreProducto2 = (input("¿Que otro producto quiere comprar? "))
    #pedir cantidad producto2
    cantidadProducto2 = int(input("¿Cuantos productos quieres comprar ? "))
    descuento = 1
    #calcular precio producto
    if (nombreProducto == "fruta"):
        precioProducto = precioFruta
    elif (nombreProducto == "carne"):
        precioProducto = precioCarne
    elif (nombreProducto == "pescado"):
        precioProducto = precioPescado
    elif (nombreProducto == "leche"):
        precioProducto = precioLeche
    elif (nombreProducto == "pan"):
        precioProducto = precioPan
    else:
        print("El producto no existe")

    if (diaSemana == "lunes"):
        if (nombreProducto == "fruta"):
            descuento = 0.8
    elif (diaSemana == "martes"):
        descuento = 1.2
    elif (diaSemana == "miercoles"):
        if (nombreProducto == "pescado"):
            cantidadProducto = cantidadProducto // 2 + cantidadProducto % 2
    elif (diaSemana == "viernes"):
        descuento = 0.3

    #ver cliente
    if (nombre == "carlos") or (nombre == "ines"):
        if (nombreProducto=="fruta") or (nombreProducto=="carne") or (nombreProducto=="pescado"):
            descuento -= 0.1
    elif (nombre == "mrMuro"):
        descuento = 1.5

    #calcular precio producto2
    if (nombreProducto2 == "fruta"):
        precioProducto2 = precioFruta
    elif (nombreProducto2 == "carne"):
        precioProducto2 = precioCarne
    elif (nombreProducto2 == "pescado"):
        precioProducto2 = precioPescado
    elif (nombreProducto2 == "leche"):
        precioProducto2 = precioLeche
    elif (nombreProducto2 == "pan"):
        precioProducto2 = precioPan

    #calcular precio total
    precioTotal = (precioProducto * cantidadProducto + precioProducto2 * cantidadProducto2) * descuento
else:
    print(mensaje)

print("El precio total es", precioTotal, "€")
print("Gracias por su compra, esperamos verle pronto")

