#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

#Pedimos el día
dia = input("Día: ")

#Pedimos el mes
mes = input("Mes: ")

#Pedimos el año
año = input("Año: ")

#Condiciones: 

if (mes=="1" or mes=="3" or mes=="5" or mes=="7" or mes=="8" or mes=="10" or mes=="12"):
    if (dia>0 and dia<=31):
        print("La fecha es correcta")
    else:
        print("La fecha no es correcta")
elif (mes=="4" or mes=="6" or mes=="9" or mes=="11"):
    if dia>0 and dia<=30:
        print("La fecha es correcta")
    else:
        print("La fecha no es correcta")    
elif (mes=="2"):
    if dia>0 and dia<=28:
        print("La fecha es correcta")
    elif (dia==29 and (año % 4==0 and año % 100 !=0 or año % 400==0)):
        print("La fecha es correcta")
    else:
        print("La fecha no es correcta")   

        #Condicion bisisesto: año % 4==0 and año % 100 !=0 or año % 400==0