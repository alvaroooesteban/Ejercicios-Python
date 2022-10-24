#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas
#horas y minutos corresponde.

dato=int(input("Introduzca la cantidad de minutos que quiera convertir: "))
hora=dato//60
minutos=dato % 60
print("Horas:", hora, "Minutos:", minutos)