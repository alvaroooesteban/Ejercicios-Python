#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
#Calcula y muestra la distancia entre ellos.

import math
print("Dime las coordenadas del  primer punto :")
x1 = int(input())
y1 = int(input())
print("Dime las coordenadas del segundo punto :")
x2 = int(input())
y2 = int(input())
distancia = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print("La distancia es :",distancia)
