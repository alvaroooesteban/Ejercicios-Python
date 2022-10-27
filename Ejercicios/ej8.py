#Pedir nota,edad,sexo:
nota=int(input("Introduzaca nota: "))
edad=int(input("Introduzca edad edad: "))
sexo=input("Introduzca sexo: ").upper()

#Condiciones: 
if (nota >=5 and edad >=18 and sexo =="F"):
    print("aprobada")
#elif (nota >=5 and edad >=18 and sexo =="M"): (Fuerza bruta, está mal)
elif sexo =="M":
    print("posible")
else:
    print("no aceptada")
#elif (nota < 5 and edad <18 ):
    #print("no aceptada")