#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el
#vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres
#ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
#base y comisiones.

salario_base=int(input("Introduzca su salario base:" ))
comision=(salario_base*0.10)
salario_total=salario_base+(comision)*3
print("Su salario total es de: ", salario_total, "€", ",su salario base es de: ", salario_base ,"€", "y su comision es de:", comision ,"€") 
