#Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

#datos:
horas = 0
minutos = 0
segundos = 0

#proceso:
for i in range(1, 86400):
    segundos = segundos + 1
    if segundos == 60:
        segundos = 0
        minutos = minutos + 1
    if minutos == 60:
        minutos = 0
        horas = horas + 1
    if horas == 24:
        horas = 0
    print(horas, ":", minutos, ":", segundos)
    