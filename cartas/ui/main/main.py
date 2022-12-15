from domain.modelo.jugador import Jugador
from domain.modelo.baraja import Baraja
from domain.servicios.servicios_cartas import ServiciosCartas


# ejecucion cosas
def main():
    serviciosCartas = ServiciosCartas()
    baraja : Baraja = serviciosCartas.crear_baraja()

    serviciosCartas.mezclar_baraja(baraja.cartas)
    
    #Pedir 2 jugadores
    nombre=input("Introduce el nombre del jugador : ")
    apellido=input("Introduce el apellido del jugador : ")
    jugador1: Jugador = Jugador(nombre,apellido)
    nombre=input("Introduce el nombre del jugador : ")
    apellido=input("Introduce el apellido del jugador : ")
    jugador2: Jugador = Jugador(nombre,apellido)
    # Combat cartas


    # sacar una carta para cada jugador
    carta_judador1=baraja.siguiente_carta()
    carta_jugador2=baraja.siguiente_carta()
    for i in range(0,40,2):
        carta_judador1=baraja.cartas[i]
        carta_jugador2=baraja.cartas[i+1]
        print("La carta del jugador 1 es",carta_judador1,"y la del jugador 2 es",carta_jugador2) 
        if carta_judador1.valor.value > carta_jugador2.valor.value:
            jugador1.puntos+=1
            print("El jugador 1 gana la ronda")
        elif carta_judador1.valor.value < carta_jugador2.valor.value:
            jugador2.puntos+=1
            print("El jugador 2 gana la ronda")
        else:
            print("Empate")
    print("El jugador 1 tiene",jugador1.puntos,"puntos")
    print("El jugador 2 tiene",jugador2.puntos,"puntos")
    print("El ganador es",jugador1.nombre_completo()) if jugador1.puntos > jugador2.puntos else print("El ganador es",jugador2.nombre_completo())

    #un punto al jugador que la tenga mas grande

    # al final cuando se acaba la baraja se dice quien gana


    
   
