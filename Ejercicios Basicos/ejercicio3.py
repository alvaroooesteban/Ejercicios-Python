#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math

cateto1= int(input("Introduzca la medidida de uno de los catetos: "))
cateto2= int(input("Introduzca la medida del otro cateto: "))

suma_cuadrado_catetos=(cateto1**2 + cateto2**2)
hipotenusa=math.sqrt(suma_cuadrado_catetos)

print("La hipotenusa es:", hipotenusa)