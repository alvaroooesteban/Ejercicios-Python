#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
#pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

moneda_2e=int(input("Monedas de 2 euros:"))
moneda_1e=int(input("Monedas de 1 euro:"))
moneda_50cent=int(input("Monedas de 50 céntimos:"))
moneda_20cent=int(input("Monedas de 20 céntimos:"))
moneda_10cent=int(input("Monedas de 10 céntimos:"))

#Calcular Euros:

euros_totales = moneda_2e * 2 + moneda_1e

#Calcular centimos: 

centimos_totales = moneda_50cent * 50 + moneda_20cent * 20 + moneda_10cent * 10

#Convertir centimos a euros:

total_euros= euros_totales + centimos_totales // 100
total_centimos= centimos_totales % 100

print(total_euros, "€", total_centimos, "centimos")
