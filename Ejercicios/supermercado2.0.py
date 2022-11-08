#Supermercado, 5 productos(1,2,3,4,5), el usuario compra solo dos y tiene que elegirlos. 
#Mostrar un menu con los productos y si precio y que eliga
#  El lunes el producto1 tiene 20%, el miercoles hay 2x1 del producto3, el viernes hay locura, 70% en todos. Los domingos no se abre.
#En el menu de productos tienes que avisar los descuentos que haya.
#Clientes vip, carlos, ines, en el producto 1,2,3 descuento adicional del 10%
#Cliente pufo, SrMuro paga un 50% mas, y no tiene descuentos.
#Los martes es el día de los border lines,  la factura se sube 20%.

#Establecer precio de los productos:
precio_fruta=3.50
precio_carne=5.80
precio_pescado=9.20
precio_leche=6.20
precio_pan=0.60

#diasemana:
dia_semana=0

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
nombre_cliente=input("¿Cuál es su nombre? ")
producto1=input("¿Que producto desea comprar? ")
producto2=input("¿Que otro producto desea comprar? ")

#Condicionales:
if dia_semana=="lunes":
    precio_fruta=precio_fruta*0.8

if dia_semana=="miercoles":
    precio_pescado=precio_pescado*0.5
if dia_semana=="viernes":
    precio_fruta=precio_fruta*0.3
    precio_carne=precio_carne*0.3
    precio_pescado=precio_pescado*0.3
    precio_leche=precio_leche*0.3
    precio_pan=precio_pan*0.3
if dia_semana=="domingo":
    print("Cerrado")
if dia_semana=="martes":
    precio_fruta=precio_fruta*1.2
    precio_carne=precio_carne*1.2
    precio_pescado=precio_pescado*1.2
    precio_leche=precio_leche*1.2
    precio_pan=precio_pan*1.2
if dia_semana=='jueves' or dia_semana=='sabado':
    print("No hay promociones")
    precio_fruta=precio_fruta
    precio_carne=precio_carne
    precio_pescado=precio_pescado
    precio_leche=precio_leche
    precio_pan=precio_pan

if nombre_cliente=="carlos" or nombre_cliente=="ines":
        precio_fruta=precio_fruta*0.9
        precio_carne=precio_carne*0.9
        precio_pescado=precio_pescado*0.9
elif nombre_cliente=="SrMuro":
        precio_fruta=precio_fruta*1.5
        precio_carne=precio_carne*1.5
        precio_pescado=precio_pescado*1.5
        precio_leche=precio_leche*1.5
        precio_pan=precio_pan*1.5
else:  
        precio_fruta=precio_fruta
        precio_carne=precio_carne
        precio_pescado=precio_pescado
        precio_leche=precio_leche
        precio_pan=precio_pan
if producto1=="fruta":
        precio_producto1=precio_fruta
        print("El precio de la fruta es", precio_fruta,"€")
elif producto1=="carne":
        precio_producto1=precio_carne
        print("El precio de la carne es", precio_carne,"€")
elif producto1=="pescado":
        precio_producto1=precio_pescado
        print("El precio de la carne es", precio_pescado, "€")
elif producto1=="leche":
        precio_producto1=precio_leche
        print("El precio de la carne es", precio_leche, "€")
elif producto1=="pan":
        precio_producto1=precio_pan
        print("El precio de la carne es", precio_pan, "€")
else:
        print("Error, producto seleccionado no existe")

if producto2=="fruta":
        precio_producto2=precio_fruta 
        print("El precio de la fruta es", precio_fruta,"€")  
elif producto2=="carne":
        precio_producto2=precio_carne
        print("El precio de la carne es", precio_carne,"€")
elif producto2=="pescado":
        precio_producto2=precio_pescado
        print("El precio de la carne es", precio_pescado, "€")
elif producto2=="leche":
        precio_producto2=precio_leche
        print("El precio de la carne es", precio_leche, "€")
elif producto2=="pan":
        precio_producto2=precio_pan
        print("El precio de la carne es", precio_pan, "€")
else:
        print("Error, producto seleccionado no existe")

print("Deseamos que vuelva pronto")