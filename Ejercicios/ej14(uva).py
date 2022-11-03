#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se
#clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto,
#ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la
#uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
#se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
#tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
#cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

#Pedir datos:
cantidad=int(input("Introduzaca la cantidad en kg: "))
precioInicial=float(input("Introduzca el precio inicial: "))
tipoUva=input("Introduzca el tipo de uva: ")
sizeUva=int(input("Introduzca el tamaño de la uva: "))


#condiciones:
if (tipoUva=="A" and sizeUva==1):
        print(cantidad*precioInicial+0.20, "€")

elif  sizeUva==2:
        print((cantidad*precioInicial+0.30), "€")

elif (tipoUva=="B" and sizeUva==1):
     print(cantidad*precioInicial-0.30, "€")
elif  sizeUva==2:
     print((cantidad*precioInicial-0.50), "€")


     ##Error en el tipo 2
     #Correccciones:
     if tipoUva=="A":
        if sizeUva==1:
            print(cantidad*precioInicial+0.20, "€")
        elif sizeUva==2:
            print((cantidad*precioInicial+0.30), "€")
        elif tipoUva=="B":
                if sizeUva==1:
                        print(cantidad*precioInicial-0.30, "€")
                elif sizeUva==2:
                        print((cantidad*precioInicial-0.50), "€")
                else:
                        print("Error en el tamaño")