#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un
#dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara
#opuesta al resultado obtenido.
#•Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y
#3-4.
#•Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará
#el mensaje: “ERROR: número incorrecto.”.

#Pedir datos:
numeroCaraDados = int(input("Introduzca el numero de la cara del dado: "))

#Condiciones:
if numeroCaraDados == 1:
    print("La cara opuesta es el seis")
elif numeroCaraDados == 2:
    print("La cara opuesta es el cinco")
elif numeroCaraDados == 3:
    print("La cara opuesta es el cuatro")
elif numeroCaraDados == 4:
    print("La cara opuesta es el tres")
elif numeroCaraDados == 5:
    print("La cara opuesta es el dos")
elif numeroCaraDados == 6:
    print("La cara opuesta es el uno")
else:
    print("ERROR: numero incorrecto")

    #Otra forma de hacerlo:
    numeroCaraDados = int(input("Introduzca el numero de la cara del dado: "))
    caraOpuesta = ""
    hayError = False
#Sacamos la cara opuesta:
    if numeroCaraDados == 1:
        caraOpuesta = "seis"   
    elif numeroCaraDados == 2:
        caraOpuesta = "cinco"
    elif numeroCaraDados == 3:
        caraOpuesta = "cuatro"
    elif numeroCaraDados == 4:
        caraOpuesta = "tres"
    elif numeroCaraDados == 5:
        caraOpuesta = "dos"
    elif numeroCaraDados == 6:
        caraOpuesta = "uno"
    else:
        hayError = True
#salida del programa:
if not hayError:
    print("La cara opuesta es : ",  caraOpuesta)
else:
    print("ERROR: numero incorrecto")