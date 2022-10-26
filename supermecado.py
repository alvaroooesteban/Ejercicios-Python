#Establecer precio de los productos:

precio_fruta=float(3.50)
precio_carne=float(5.80)
precio_pescado=float(9.20)
precio_leche=float(6.20)
precio_pan=float(0.60)

#Pedir cantidaddes 
cantidad_fruta=int(input("Introduzca la cantidad de fruta comprada: "))
cantidad_carne=int(input("Introduzca la cantidad de carne comprada: "))
cantidad_pescado=int(input("Introduzca la cantidad de pescado comprada: "))
cantidad_leche=int(input("Introduzca la cantidad de leche comprada: "))
cantidad_pan=int(input("Introduzca la cantidad de pan comprada: "))

#Calcular el total e imprimir el resultado: 
total=(precio_fruta*cantidad_fruta) + (cantidad_carne*precio_carne) + (precio_pescado*cantidad_pescado) + (precio_leche*cantidad_leche) + (precio_pan*cantidad_pan)

print("El total de su compra es de :" , total, "€.")
