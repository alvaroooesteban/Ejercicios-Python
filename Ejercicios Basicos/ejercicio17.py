#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de
#viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la
#hora de llegada a la ciudad B.

hora_salida=int(input("Hora de salida: "))
minuto_salida=int(input("Minutos de salida: "))
segundos_salida=int(input("Segundos de salida: "))
segundos_viaje= int(input("Tiempo que has tardado en segundos:"))

#Conversion a segundos:
segundos_inicio=hora_salida*3600 + minuto_salida*60 + segundos_salida

#Sumamamos los segundos: 
segundos_final=  segundos_inicio + segundos_viaje 

#Conversiuon de los segundos a horas,minutos,segundos:
hora_llegada=segundos_final//3600
minuto_llegada=(segundos_final % 3600)// 60
segundos_llegada=(segundos_final % 3600) % 60

print("Hora de llegada: ",hora_llegada, ":",minuto_llegada,":",segundos_llegada )