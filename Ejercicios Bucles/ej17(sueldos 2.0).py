#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
#Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo
#para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la
#empresa por los N empleados.

#datos:
n = int(input("Ingrese la cantidad de empleados: "))
sueldos = []
horas = []

#proceso:
for i in range(1, n + 1):
    print("Ingrese las horas trabajadas por el empleado", i)
    for j in range(1, 8):
        horas.append(int(input("Ingrese las horas trabajadas el día " + str(j) + ": ")))
    sueldos.append(sum(horas) * 20000)
    horas = []

#salida:
for i in range(1, n + 1):
    print("El empleado", i, "trabajó", sueldos[i - 1] / 20000, "horas y cobró", sueldos[i - 1], "€")
print("La empresa pagó", sum(sueldos), "€")
