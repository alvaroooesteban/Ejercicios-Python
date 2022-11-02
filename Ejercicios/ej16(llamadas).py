#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
#es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
#los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
#décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de
#mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe
#pagar por cada concepto una persona que realiza una llamada.

#Definicion de variables:
tiempoLlamada = int(input("Introduzca el tiempo de la llamada en minutos: "))
precioLlamada = 1
turno = input("Introduzca el turno de trabajo: ")
dia = input("Introduzca el dia de la semana: ")

#Condiciones:
if (tiempoLlamada<=5):
    print("El precio de la llamada es de", precioLlamada, "€")
elif (tiempoLlamada>5 and tiempoLlamada<=8):
        print("El precio de la llamada es de", precioLlamada+0.80, "€")
elif (tiempoLlamada>8 and tiempoLlamada<=10):
        print("El precio de la llamada es de", precioLlamada+1.50, "€")
elif (tiempoLlamada>10):
        print("El precio de la llamada es de", precioLlamada+2, "€")

if (dia=="domingo"):
    print("El precio de la llamada es de", precioLlamada+0.03, "€")
    
if(dia!="domingo" and turno=="mañana"):
    print("El precio de la llamada es de", precioLlamada+0.15, "€")
elif (turno=="tarde"):
        print("El precio de la llamada es de", precioLlamada+0.10, "€")

        ##Error