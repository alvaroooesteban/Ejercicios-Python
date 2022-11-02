#Escribe un programa que pida un número entero entre uno y doce e imprima el número de
#días que tiene el mes correspondiente.

#pedir datos
numeroMes=int(input("ingrese un numero del 1 al 12:"))
#condicionales
if numeroMes==1:
    print("Enero tiene 31 dias")
elif numeroMes==2:
    print("Febrero tiene 28 dias")
elif numeroMes==3:
    print("Marzo tiene 31 dias")
elif numeroMes==4:
    print("Abril tiene 30 dias")
elif numeroMes==5:
    print("Mayo tiene 31 dias")
elif numeroMes==6:
    print("Junio tiene 30 dias")
elif numeroMes==7:
    print("Julio tiene 31 dias")
elif numeroMes==8:
    print("Agosto tiene 31 dias")
elif numeroMes==9:
    print("Septiembre tiene 30 dias")
elif numeroMes==10:
    print("Octubre tiene 31 dias")
elif numeroMes==11:
    print("Noviembre tiene 30 dias")
elif numeroMes==12:
        print("Diciembre tiene 31 dias")
else:
    print("Error, solo hay 12 meses en un año")

    