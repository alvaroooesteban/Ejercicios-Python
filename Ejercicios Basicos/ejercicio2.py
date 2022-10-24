#Calcular el perímetro y área de un rectángulo dada su base y su altura.
base= int(input("¿Cuanto mide la base? ") )
altura= int(input("¿Cual es la altura? "))

perimetro= base+base+altura+altura
print("El perímetro es:", perimetro)
area= base * altura 
print("El área es:",area)