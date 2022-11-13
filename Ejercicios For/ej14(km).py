#Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km
#150, los coches tienen sentido opuesto y tienen la misma velocidad. Realizar un programa
#para determinar en qué kilómetro de esa carretera se encontrarán.

#datos:
km1 = 70
km2 = 150
velocidad = int(input("Ingrese la velocidad de los coches: "))

#proceso:
distancia = km2 - km1
tiempo = distancia / velocidad
km3 = km2 + (velocidad * tiempo)

#salida:
print("Los coches se encontrarán en el km", km3)
