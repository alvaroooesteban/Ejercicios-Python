#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
#cuanto deberá pagar finalmente por su compra.

precio_compra=int(input("Introduzca el precio de su compra: "))
descuento=precio_compra*0.15
precio_final=precio_compra-descuento
print("El precio final de su compra es de: ",precio_final, "€")