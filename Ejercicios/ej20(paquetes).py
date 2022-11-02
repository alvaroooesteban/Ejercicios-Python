#Una compañía de transporte internacional tiene servicio en algunos países de América del
#Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transportese basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la
#tabla:
#Zona Ubicación Costo/gramo
#1 América del Norte 24.00 euros
#2 América Central 20.00 euros
#3 América del Sur 21.00 euros
#4 Europa 10.00 euros
#5 Asia 18.00 euros
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son
#transportados, esto por cuestiones de logística y de seguridad.
#Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el
#rechazo de la entrega.

#Pedir datos:
pesoPaquete = float(input("Ingrese el peso del paquete: "))
zonaDestino = int(input("Ingrese la zona de destino: "))

#Condiciones:
if pesoPaquete < 5:
    print("El paquete  puede ser transportado")
else:
    print("El paquete  no puede ser transportado")

if zonaDestino == 1:
        print("El costo del envio es: ", pesoPaquete * 24)
elif zonaDestino == 2:
        print("El costo del envio es: ", pesoPaquete * 21)    
elif zonaDestino == 3:
        print("El costo del envio es: ", pesoPaquete * 18)
elif zonaDestino == 4:
        print("El costo del envio es: ", pesoPaquete * 16)
elif zonaDestino == 5:
        print("El costo del envio es: ", pesoPaquete * 14)
else:
    print("Error, solo hay 5 zonas de destino")

    #Error
    