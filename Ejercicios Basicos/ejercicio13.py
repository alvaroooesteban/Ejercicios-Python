#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
#Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se
#puede calcular?

import math
numero = int(input("Dime el número:"))
print("Raíz cuadrada:",math.sqrt(numero))
print("Raíz cúbica:",numero ** (1 / 3))
