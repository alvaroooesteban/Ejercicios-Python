#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
#Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule
#cuánto pagó la empresa por los N empleados.

#datos:
n = int(input("Ingrese la cantidad de empleados: "))
sueldos = []
horas = []

#proceso:
for i in range(1, n + 1):
    horas.append(int(input("Ingrese las horas trabajadas por el empleado " + str(i) + ": ")))
    sueldos.append(horas[i - 1] * 20000)

#salida:
for i in range(1, n + 1):
    print("El empleado", i, "trabajó", horas[i - 1], "horas y cobró", sueldos[i - 1], "€")
print("La empresa pagó", sum(sueldos), "€")
