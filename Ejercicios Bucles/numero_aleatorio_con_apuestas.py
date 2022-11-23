#Adivinar un numero aleatorio entre 1 y 100 apostando dinero:
import random
numeroAleatorio = random.randint(1, 100)
numeroIntentos = 0
jugando = False
cantidadDinero = 0
apuesta= 0
quererJugar= True

print("Bienvenido al juego de adivinar el número")
print("El número está entre 1 y 100 y tienes 10 intentos para adivinarlo")
print("Si adivinas el numero, ganas lo apostado, si no, pierdes lo apostado")
print("¿Desea jugar (si/no)? ")
respuesta = input("Introduzca su respuesta: ")
while respuesta != "no":
    cantidadDinero= int(input("Introduzca la cantidad de dinero que tiene: "))
    while cantidadDinero > 0:
        jugando= True
        apuesta = int(input("¿Qué cantidad de dinero desea apostar? "))
        if (apuesta <= cantidadDinero):
                print("Apuesta aceptada")
                jugando = True
                while jugando:
                    numeroIntentos += 1
                    if numeroIntentos <=10: 
                        eleccion = int(input("Introduzca un numero: "))
                        if eleccion == numeroAleatorio:
                            cantidadDinero += apuesta
                            print("Has ACERTADO, tienes "+str(cantidadDinero)+"€")
                            print("Has necesitado", numeroIntentos, "intentos para acertar el número") 
                            numeroIntentos=0
                            respuesta=input("¿Quieres seguir jugando? (si/no) ")
                            if respuesta == "si":
                                        quererJugar = True  
                                        input("¿Cuanto dinero quieres apostar?")
                        
                            elif respuesta == "no":
                                quererJugar = False
                                print("Gracias por jugar, hasta la próxima")
                                exit()
                        elif eleccion > numeroAleatorio:
                            print("El numero es MENOR, llevas", numeroIntentos , "intentos")
                            jugando = True
                        elif eleccion < numeroAleatorio:
                                print("El numero es MAYOR, llevas", numeroIntentos , "intentos")
                                jugando = True
                    else:
                        cantidadDinero -= apuesta
                        print("Has FALLADO, tienes "+str(cantidadDinero)+"€")
                        numeroIntentos=0
                        if cantidadDinero <= 0:
                            print("No tienes dinero para seguir jugando, hasta la próxima")
                            exit()
                        respuesta=input("¿Quieres seguir jugando? (si/no) ")
                        if respuesta == "si":
                            quererJugar = True  
                            input("¿Cuanto dinero quieres apostar?")
                        elif respuesta == "no":
                                quererJugar = False
                                print("Gracias por jugar, hasta la próxima")
                                exit()
                        
        elif (apuesta > cantidadDinero):
                print("Apuesta denegada, no tines suficiente dinero")
                jugando = False
        elif (apuesta == 0):
                print("Apuesta denegada, no puedes apostar 0")
                jugando = False
                exit()
    if cantidadDinero <= 0:
        print("No tienes dinero para jugar, hasta la próxima")
        exit()                

print("Esperemos que vuelvas pronto")


