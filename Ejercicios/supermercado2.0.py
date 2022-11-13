#El programa imprime el precio de los productos establecidos en ##Establecer precio de los productos, no hace las operaciones de las condiciones de los descuentos

#Establecer precio de los productos:
precioFruta=3.50
precioCarne=5.80
precioPescado=9.20
precioLeche=6.20
precioPan=0.60

#diasemana:
diaSemana=0

#precio productos:
precioProducto1=0
precioProducto2=0

#MENU DE PRODUCTOS
print("Bienvenido al supermercado 2.0, nuestros productos son:")
print("1. Fruta")
print("2. Carne")
print("3. Pescado")
print("4. Leche")
print("5. Pan")

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


#Pedir datos:

input("¿Que dia es hoy? ")
nombreCliente=input("¿Cuál es su nombre? ")
producto1=input("¿Que producto desea comprar? ")
producto2=input("¿Que otro producto desea comprar? ")

#Condicionales:
if diaSemana=="lunes":
        precioFruta=precioFruta*0.8
        precioCarne=precioCarne
        precioLeche=precioLeche
        precioLpan=precioPan
        precioPescado=precioPescado
        if nombreCliente=="carlos" or nombreCliente=="ines":
                precioFruta=precioFruta*0.9
                precioCarne=precioCarne*0.9
                precioLeche=precioLeche*0.9
                precioLpan=precioPan*0.9
                precioPescado=precioPescado*0.9
        elif nombreCliente=="SrMuro":
                precioFruta=precioFruta*1.5
                precioCarne=precioCarne*1.5
                precioLeche=precioLeche*1.5
                precioLpan=precioPan*1.5
                precioPescado=precioPescado*1.5
        else:
                precioFruta=precioFruta
                precioCarne=precioCarne
                precioLeche=precioLeche
                precioLpan=precioPan
                precioPescado=precioPescado
elif diaSemana=="miercoles":
        precioPescado=precioPescado*0.5
        precioCarne=precioCarne
        precioFruta=precioFruta
        precioLeche=precioLeche
        precioPan=precioPan
        if nombreCliente=="carlos" or nombreCliente=="ines":
                precioFruta=precioFruta*0.9
                precioCarne=precioCarne*0.9
                precioLeche=precioLeche*0.9
                precioLpan=precioPan*0.9
                precioPescado=precioPescado*0.9
        elif nombreCliente=="SrMuro":
                precioFruta=precioFruta*1.5
                precioCarne=precioCarne*1.5
                precioLeche=precioLeche*1.5
                precioLpan=precioPan*1.5
                precioPescado=precioPescado*1.5
elif diaSemana=="viernes":
        precioFruta=precioFruta*0.3
        precioCarne=precioCarne*0.3
        precioPan=precioPan*0.3
        precioLeche=precioLeche*0.3
        precioPescado=precioPescado*0.3
        if nombreCliente=="carlos" or nombreCliente=="ines":
                precioFruta=precioFruta*0.9
                precioCarne=precioCarne*0.9
                precioLeche=precioLeche*0.9
                precioLpan=precioPan*0.9
                precioPescado=precioPescado*0.9
        elif nombreCliente=="SrMuro":
                precioFruta=precioFruta*1.5
                precioCarne=precioCarne*1.5
                precioLeche=precioLeche*1.5
                precioLpan=precioPan*1.5
                precioPescado=precioPescado*1.5
elif diaSemana=="domingo":
    print("Cerrado")
elif diaSemana=="martes":
        print("Dia de los boerline: 20% de subida en la factura")
        precioFruta=precioFruta*1.2
        precioCarne=precioCarne*1.2
        precioPan=precioPan*1.2
        precioLeche=precioLeche*1.2
        precioPescado=precioPescado*1.2
        if nombreCliente=="carlos" or nombreCliente=="ines":
                precioFruta=precioFruta*0.9
                precioCarne=precioCarne*0.9
                precioLeche=precioLeche*0.9
                precioLpan=precioPan*0.9
                precioPescado=precioPescado*0.9
        elif nombreCliente=="SrMuro":
                precioFruta=precioFruta*1.5
                precioCarne=precioCarne*1.5
                precioLeche=precioLeche*1.5
                precioLpan=precioPan*1.5
                precioPescado=precioPescado*1.5
elif diaSemana=='jueves' or diaSemana=='sabado':
        precioFruta=precioFruta
        precioCarne=precioCarne
        precioPan=precioPan
        precioLeche=precioLeche
        precioPescado=precioPescado
        if nombreCliente=="carlos" or nombreCliente=="ines":
                precioFruta=precioFruta*0.9
                precioCarne=precioCarne*0.9
                precioLeche=precioLeche*0.9
                precioLpan=precioPan*0.9
                precioPescado=precioPescado*0.9
        elif nombreCliente=="SrMuro":
                precioFruta=precioFruta*1.5
                precioCarne=precioCarne*1.5
                precioLeche=precioLeche*1.5
                precioLpan=precioPan*1.5
                precioPescado=precioPescado*1.5


if producto1=="fruta":
        precioProducto1=precioFruta
        if diaSemana=="lunes":
                precioProducto1=precioFruta*0.8
        elif diaSemana=="marte":
                precioProducto1=precioFruta*1.2
        print("El precio de la fruta es", precioProducto1,"€")
elif producto1=="carne":
                precioProducto1=precioCarne
                print("El precio de la carne es", precioProducto1,"€")
elif producto1=="pescado":
                precioProducto1=precioPescado
                print("El precio del pescado es", precioProducto1,"€")
elif producto1=="leche":
                precioProducto1=precioLeche
                print("El precio de la leche es", precioProducto1,"€")
elif producto1=="pan":
                precioProducto1=precioPan
                print("El precio del pan es", precioProducto1,"€")
else:
        print("Error, producto seleccionado no existe")

if producto2=="fruta":
        precioProducto2=precioFruta
        print("El precio de la fruta es", precioProducto2,"€")
elif producto2=="carne":
                precioProducto2=precioCarne
                print("El precio de la carne es", precioProducto2,"€")
elif producto2=="pescado":
                precioProducto2=precioPescado
                print("El precio del pescado es", precioProducto2,"€")
elif producto2=="leche":
                precioProducto2=precioLeche
                print("El precio de la leche es", precioProducto2,"€")
elif producto2=="pan":
                precioProducto2=precioPan
                print("El precio del pan es", precioProducto2,"€")
else:
        print("Error, producto seleccionado no existe")

print("Deseamos que vuelva pronto")