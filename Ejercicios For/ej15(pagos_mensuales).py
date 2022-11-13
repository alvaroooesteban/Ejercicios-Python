#Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
#segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo para determinar
#cuánto debe pagar mensualmente y el total de
#lo que pagó después de los 20 meses.

#datos:
meses = 20
precio = 10

#proceso:
for i in range(1, meses + 1):
    print("Mes", i, "pago", precio, "€")
    precio = precio * 2

#salida:
print("Total pagado:", precio / 2)
