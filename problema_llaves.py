tenerLlave=input('¿Tienes una llave? ')
if tenerLlave=='si':
    forma=input('¿Que forma tiene la llave? ')
    color=input('¿Que color tiene la llave? ')
    if forma=='circulo' and color=='rojo':
        print('Pasa por la puerta A')
    elif forma=='cuadrado' and color=='azul':
        print('Pasa por la puerta B')
    else:
        print('No tirnes acceso a ninguna puerta, llave incorrecta')
elif tenerLlave=='no':
    print('No tines llave, busca una y vuelve')
else: print('Error, no se reconoce la respuesta')
print('Adios')