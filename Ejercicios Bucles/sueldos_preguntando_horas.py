#pedir numero trabajadores:
numeroTrabajadores = int(input("¿Cuantos trabajadores hay en la empresa? "))

costeSemanalEmpresa = 0

for i in range(numeroTrabajadores):
    #pedir sueldo un trabajador:
    print("Trabajador "+str(i+1))
    sueldo = float(input("¿Cual es su sueldo por hora? "))
    #pedir numero de dias trabajados y numero de horas cada dia:
    diasTrabajados = int(input("¿Cuantos dias ha trabajado? "))
    for j in range(1,diasTrabajados+1):
        horasTrabajadas=(int(input("Ingrese las horas trabajadas el día " + str(j) + ": ")))
    sueldoDeTrabajador = sueldo * diasTrabajados * horasTrabajadas
    print("El sueldo de este trabajador es "+str(sueldoDeTrabajador))
    costeSemanalEmpresa += sueldoDeTrabajador
   

print("El coste semanal de la empresa es "+str(costeSemanalEmpresa), "€")
#Mal,no se acumulan las horas trabajadas

#Correcto:
#pedir numero trabajadores
numeroTrabajadores = int(input("¿Cuantos trabajadores hay en la empresa? "))

costeSemanalEmpresa = 0

for i in range(numeroTrabajadores):
    #pedir sueldo un trabajador
    print("Trabajador "+str(i+1))
    sueldo = float(input("¿Cual es su sueldo por hora? "))
    #pedir numero de dias trabajados
    diasTrabajados = int(input("¿Cuantos dias ha trabajado? "))
    #pedir horas cada dia
    horasTrabajadasEmpleadoALaSemana = 0
    for i in range(diasTrabajados):
        horasTrabajadasPorDia = float(input("¿Cuantas horas ha hecho cada dia? "))
        horasTrabajadasEmpleadoALaSemana += horasTrabajadasPorDia
        
    sueldoDeUnTrabajador = sueldo*horasTrabajadasEmpleadoALaSemana*diasTrabajados
    print("El sueldo de este trabajador es "+str(sueldoDeUnTrabajador))
    costeSemanalEmpresa += sueldoDeUnTrabajador

print("El coste semanal de la empresa es "+str(costeSemanalEmpresa))