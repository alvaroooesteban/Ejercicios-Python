#Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de
#números primos que queremos mostra

#datos:
cantidadNumerosPrimos = int(input("Ingrese la cantidad de números primos que quiere mostrar: "))
numeros = []
numerosPrimos = []
contador = 0
numero = 2

#proceso:
while contador < cantidadNumerosPrimos :
    for i in range(1, numero + 1):
        if numero % i == 0:
            numeros.append(i)
    if len(numeros) == 2:
        numerosPrimos.append(numero)
        contador = contador + 1
    numeros = []
    numero = numero + 1

#salida:
print(numerosPrimos)
