import random
numeroAleatorio = random.randint(1, 100)
numeroIntentos = 0
cantidadDinero = 0
apuesta= 0
jugar= False
quererJugar= True


print("Bienvenido al juego de adivinar el número")
print("El número está entre 1 y 100 y tienes 10 intentos para adivinarlo")
print("Si adivinas el numero, ganas lo apostado, si no, pierdes lo apostado")
print("¿Desea jugar (si/no)? ")
respuesta = input("Introduzca su respuesta: ")

while respuesta != "no":
    cantidadDinero = int(input("Introduzca la cantidad de dinero que tiene: "))
    apuesta=int(input("¿Cuanto dinero quieres apostar? "))
    if cantidadDinero > apuesta :
        print("Apuesta aceptada")
    elif cantidadDinero < apuesta:
        print("No tienes suficiente dinero, introduce una cantidad valida")
        jugar = True
    while jugar:
        numeroIntentos += 1
    numeroElegido = int(input("Introduzca un numero: "))
    if numeroIntentos <= 10:
            if numeroElegido > numeroAleatorio:
                print("El numero es MENOR, te quedan", numeroIntentos, "intentos")
            elif numeroElegido < numeroAleatorio:
                print("El numero es MAYOR, te quedan", numeroIntentos, "intentos")
            elif numeroElegido == numeroAleatorio:
                print("Has ACERTADO, tienes "+str(cantidadDinero)+"€")
                print("Has necesitado", numeroIntentos, "intentos para acertar el número")
        
                
                respuesta=input("¿Quieres seguir jugando? (si/no) ")
                if respuesta == "si":
                    quererJugar = True  
                    input("¿Cuanto dinero quieres apostar?")
                elif respuesta == "no":
                    quererJugar = False
                    print("Gracias por jugar, hasta la próxima")
                    exit()

print("Esperemos que vuelvas pronto")
