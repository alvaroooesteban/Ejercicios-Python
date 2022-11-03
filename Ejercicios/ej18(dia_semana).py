#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
#correspondiente. Si introducimos otro número nos da un error.

#Pedimos el día de la semana
diaSemana = int(input("Introduce el día de la semana: "))

#Condiciones
if diaSemana == 1:
    print("Lunes") 
elif diaSemana == 2:
    print("Martes")
elif diaSemana == 3:
    print("Miércoles")
elif diaSemana == 4:
    print("Jueves")
elif diaSemana == 5:
    print("Viernes")
elif diaSemana == 6:
    print("Sábado")
elif diaSemana == 7:
    print("Domingo")     
else:
    print("Error, solo hay 7 días en la semana")