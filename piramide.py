#Enunciado:
#     *
#    **
#   ***
#  ****
# *****


#Piramide normal:
numero = int(input("Dime un numero: "))

for i in range (1,numero+1):
    mensaje = ""
    for j in range (i):
        mensaje  +=  "*"
    print (mensaje)


#Piramide invertida:
numero = int(input("Dime un numero: "))
for i in range (numero):
    mensaje = ""
    for j in range (numero-i):
        mensaje  +=  "*"
    print (mensaje)

#Piramide con espacios (Lo que se pide en el enunciado):
numero = int(input("Dime un numero: "))
for i in range (1,numero+1):
    mensaje = ""
    for j in range (numero-i):
        mensaje  +=  " "
    for j in range (i):
        mensaje  +=  "*"
    print (mensaje)

#Piramide completa:
numero = int(input("Dime un numero: "))
for i in range (1,numero+1):
    mensaje = ""
    for j in range (numero-i):
        mensaje  +=  " "
    for j in range (i):
        mensaje  +=  "*"
    for j in range (i-1):
        mensaje  +=  "*"
    print (mensaje)
    
