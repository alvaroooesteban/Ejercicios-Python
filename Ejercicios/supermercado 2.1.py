#El programa no imprime el precio total de las condiciones, solo imprime el precioProducto 1=0 y el precioProducto 2=0. 
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

#Pedir datos:
input("¿Que dia es hoy? ")
nombreCliente=input("¿Cuál es su nombre? ")
producto1=input("¿Que producto desea comprar? ")
producto2=input("¿Que otro producto desea comprar? ")

#Condicionales:
if producto1=="fruta":
    if diaSemana=="lunes":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto1=3.50*0.8*0.9
        elif nombreCliente=="srmuro":
            precioProducto1=3.50*1.5
        else:
            precioProducto1=3.50*0.8
   
    if diaSemana=="martes":
        if diaSemana=="martes":
           if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto1=3.50*1.2*0.9
           elif nombreCliente=="srmuro":
            precioProducto1=3.50*1.2*1.5
    else:
            precioProducto1=3.50*1.2
   
    if diaSemana=="miercoles":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto1=3.50*0.9
        elif nombreCliente=="srmuro":
            precioProducto1=3.50*1.5
        else:
            precioProducto1=3.50
            
    if diaSemana=="jueves":
        if nombreCliente=="carlos" or nombreCliente=="ines":
          precioProducto1=3.50*0.9
        elif nombreCliente=="srmuro":
           precioProducto1=3.50*1.5
        else:
            precioProducto1=3.50
    
    if diaSemana=="viernes":    
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto1=3.50*0.3*0.9
        elif nombreCliente=="srmuro":
           precioProducto1=3.50*1.5
        else:
            precioFruta=3.50*0.3
    
    if diaSemana=="sabado":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto1=3.50*0.9
        elif nombreCliente=="srmuro":
            precioProducto1=3.50*1.5
        else:
            precioProducto1=3.50
    if diaSemana=="domingo":
        print("El supermercado esta cerrado")               
elif producto1=="carne":
    if diaSemana=="lunes":
        if nombreCliente=="carlos" or nombreCliente=="ines":
           precioProducto1=5.80*0.9
        elif nombreCliente=="srmuro":
             precioProducto1=5.80*1.5
        else:
            precioCarne=5.80 
    if diaSemana=="martes":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto1=5.80*1.2*0.9
        elif nombreCliente=="srmuro":
            precioProducto1=5.80*1.2*1.5
        else:
            precioCarne=5.80*1.2
    if diaSemana=="miercoles":
        if nombreCliente=="carlos" or nombreCliente=="ines":
           precioProducto1=5.80*0.9
        elif nombreCliente=="srmuro":
            precioProducto1=5.80*1.5
        else:
           precioProducto1=5.80 
    if diaSemana=="jueves":
        if nombreCliente=="carlos" or nombreCliente=="ines":
           precioProducto1=5.80*0.9
        elif nombreCliente=="srmuro":
            precioProducto1=5.80*1.5
        else:
            precioProducto1=5.80
    if diaSemana=="viernes":    
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto1=5.80*0.3*0.9
        elif nombreCliente=="srmuro":
           precioProducto1=5.80*1.5
        else:
            precioProducto1=5.80*0.3
    if diaSemana=="sabado":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto1=5.80*0.9
        elif nombreCliente=="srmuro":
            precioProducto1=5.80*1.5
        else:
          precioProducto1=5.80
    if diaSemana=="domingo":
        print("El supermercado esta cerrado")
elif producto1=="pescado":
    if diaSemana=="lunes":
        if nombreCliente=="carlos" or nombreCliente=="ines":
             precioProducto1=9.20*0.9
        elif nombreCliente=="srmuro":
            precioProducto1=9.20*1.5
        else:
            precioProducto1=9.20*0.8
    if diaSemana=="martes":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto1=9.20*1.2*0.9
        elif nombreCliente=="srmuro":
           precioProducto1=9.20*1.2*1.5
        else:
            precioProducto1=9.20*1.2
    if diaSemana=="miercoles":
        if nombreCliente=="carlos" or nombreCliente=="ines":
           precioProducto1=9.20*0.9
        elif nombreCliente=="srmuro":
             precioProducto1=9.20*1.5
        else:
            precioPescado=9.20
    if  diaSemana=="jueves":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto1=9.20*0.9
        elif nombreCliente=="srmuro":
          precioProducto1=9.20*1.5
        else:
            precioProducto1=9.20
    if diaSemana=="viernes":    
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto1=9.20*0.3*0.9
        elif nombreCliente=="srmuro":
            precioProducto1=9.20*1.5
        else:
            precioPescado=9.20*0.3
    if diaSemana=="sabado":
        if nombreCliente=="carlos" or nombreCliente=="ines":
           precioProducto1=9.20*0.9
        elif nombreCliente=="srmuro":
             precioProducto1=9.20*1.5
        else:
             precioProducto1=9.20
    if diaSemana=="domingo":
        print("El supermercado esta cerrado")
elif producto1=="leche":
    if diaSemana=="lunes":
        if nombreCliente=="srmuro":
             precioProducto1=6.20*1.5
        else:
            precioProducto1=6.20
    if diaSemana=="martes":
        if nombreCliente=="srmuro":
             precioProducto1=6.20*1.2*1.5
        else:
            precioProducto1=6.20*1.2        
    if diaSemana=="miercoles":
        if nombreCliente=="srmuro":
            precioProducto1=6.20*1.5
        else:
             precioProducto1=6.20
    if diaSemana=="jueves":
        if nombreCliente=="srmuro":
            precioProducto1=6.20*1.5
        else:
            precioProducto1=6.20
    if diaSemana=="viernes":    
        if nombreCliente=="srmuro":
           precioProducto1=6.20*1.5
        else:
            precioProducto1=6.20*0.3  
    if diaSemana=="sabado":
        if nombreCliente=="srmuro":
             precioProducto1=6.20*1.5
        else:
            precioProducto1=6.20
        if diaSemana=="domingo":
         print("El supermercado esta cerrado")
elif producto1=="pan":
    if diaSemana=="lunes":
        if nombreCliente=="srmuro":
            precioProducto1=0.60*1.5
        else:
           precioProducto1=0.60
    if diaSemana=="martes":
        if nombreCliente=="srmuro":
          precioProducto1=0.60*1.2*1.5
        else:
             precioProducto1=0.60*1.2    
    if diaSemana=="miercoles":
        if nombreCliente=="srmuro":
            precioProducto1=0.60*1.5
        else:
             precioProducto1=0.60
  
    if diaSemana=="jueves":
        if nombreCliente=="srmuro":
            precioProducto1=0.60*1.5
        else:
           precioProducto1=0.60    
    if diaSemana=="viernes":
        if nombreCliente=="srmuro":
            precioProducto1=0.60*1.5
        else:
            precioProducto1=0.60*0.3  
    if diaSemana=="sabado":
        if nombreCliente=="srmuro":
            precioProducto1=0.60*1.5
        else:
            precioProducto1=0.60     
    if diaSemana=="domingo":
        print("El supermercado esta cerrado")
else:
    print("El producto no existe")


if producto2=="fruta":
    if diaSemana=="lunes":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=3.50*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=3.50*1.5
        else:
            precioProducto2=3.50*0.8
    if diaSemana=="martes":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=(3.50*1.2)*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=(3.50*1.2)*1.5
        else:
            precioProducto2=3.50*1.2
    if diaSemana=="miercoles":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=3.50*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=3.50*1.5
        else:
            precioProducto2=3.50 
    if diaSemana=="jueves":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=3.50*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=3.50*1.5
        else:
            precioProducto2=3.50
    if diaSemana=="viernes":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=3.50*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=3.50*1.5
        else:
            precioProducto2=3.50*0.3
    if diaSemana=="sabado":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=3.50*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=3.50*1.5
        else:
            precioProducto2=3.50
    if diaSemana=="domingo":
        print("El supermercado esta cerrado")
elif producto2=="carne":
    if diaSemana=="lunes":
        if nombreCliente=="srmuro":
            precioProducto2=5.80*1.5
        elif nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=5.80*0.9
        else:
            precioProducto2=5.80
    if diaSemana=="martes":
        if nombreCliente=="srmuro":
            precioProducto2=5.80**1.2*1.5
        elif nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=5.80*1.2*0.9    
        else:
            precioProducto2=5.80*1.2
    if diaSemana=="miercoles":
        if nombreCliente=="srmuro":
            precioProducto2=5.80*1.5
        elif nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=5.80*0.9
        else:
            precioProducto2=5.80
    if diaSemana=="jueves":
        if nombreCliente=="srmuro":
            precioProducto2=5.80*1.5
        elif nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=5.80*0.9
        else:
            precioProducto2=precioCarne
    if diaSemana=="viernes":
        if nombreCliente=="srmuro":
            precioProducto2=5.80*1.5*0.3
        elif nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=5.80*0.9*0.3
        else:
            precioProducto2=5.80*0.3
    if diaSemana=="sabado":
        if nombreCliente=="srmuro":
            precioProducto2=5.80*1.5
        elif nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=5.80*0.9
        else:
            precioProducto2=5.80
    if diaSemana=="domingo":
        print("El supermercado esta cerrado")
elif producto2=="pescado":
    if diaSemana=="lunes":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=9.20*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=9.20*1.5
        else:
            precioProducto2=9.20
    if diaSemana=="martes":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=9.20*1.2*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=9.20*1.2*1.5
        else:
            precioProducto2=9.20*1.2
    if diaSemana=="miercoles":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=9.20*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=9.20*1.5
        else:
            precioProducto2=9.20
    if diaSemana=="jueves":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=9.20*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=9.20*1.5
        else:
            precioProducto2=9.20
    if diaSemana=="viernes":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=9.20*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=9.20*1.5
        else:
            precioProducto2=9.20*0.3
    if diaSemana=="sabado":
        if nombreCliente=="carlos" or nombreCliente=="ines":
            precioProducto2=9.20*0.9
        elif nombreCliente=="srmuro":
            precioProducto2=9.20*1.5
        else:
            precioProducto2=9.20
    if diaSemana=="domingo":
        print("El supermercado esta cerrado")
elif producto2=="leche":
    if diaSemana=="lunes":
        if nombreCliente=="srmuro":
            precioProducto2=6.20*1.5
        else:
            precioProducto2=6.20
    if diaSemana=="martes":
        if nombreCliente=="srmuro":
            precioProducto2=6.20*1.2*1.5
        else:
            precioProducto2=6.20*1.2
    if diaSemana=="miercoles":
        if nombreCliente=="srmuro":
            precioProducto2=6.20*1.5
        else:
            precioProducto2=6.20
    if diaSemana=="jueves":
        if nombreCliente=="srmuro":
            precioProducto2=6.20*1.5
        else:
            precioProducto2=6.20
    if diaSemana=="viernes":
        if nombreCliente=="srmuro":
            precioProducto2=6.20*1.5
        else:
            precioProducto2=6.20*0.3
    if diaSemana=="sabado":
        if nombreCliente=="srmuro":
            precioProducto2=6.20*1.5
        else:
            precioProducto2=6.20
    if diaSemana=="domingo":
        print("El supermercado esta cerrado")
elif producto2=="pan":
    if diaSemana=="lunes":
        if nombreCliente=="srmuro":
            precioProducto2=0.60*1.5
        else:
            precioProducto2=0.60
    if diaSemana=="martes":
        if nombreCliente=="srmuro":
            precioProducto2=0.60*1.2*1.5
        else:
            precioProducto2=0.60*1.2
    if diaSemana=="miercoles":
        if nombreCliente=="srmuro":
            precioProducto2=0.60*1.5
        else:
            precioProducto2=0.60
    if diaSemana=="jueves":
        if nombreCliente=="srmuro":
            precioProducto2=0.60*1.5
        else:
            precioProducto2=0.60
    if diaSemana=="viernes":
        if nombreCliente=="srmuro":
            precioProducto2=0.60*1.5
        else:
            precioProducto2=0.60*0.3
    if diaSemana=="sabado":
        if nombreCliente=="srmuro":
            precioProducto2=0.60*1.5
        else:
            precioProducto2=precioPan
    if diaSemana=="domingo":
        print("El supermercado esta cerrado")
else:
    print("El producto no existe")

print("El precio del producto 1 es de",precioProducto1,"euros")
print("El precio del producto 2 es de",precioProducto2,"euros")
print("El precio total es de",precioProducto1+precioProducto2,"euros")
print("Deseamos que vuelva pronto")

