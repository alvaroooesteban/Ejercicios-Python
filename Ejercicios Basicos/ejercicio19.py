#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada
#respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el
#resultado obtenido por el estudiante.

respuestas_correctas = int(input("Dime cantidad de respuestas correctas:"))
respuestas_incorrectas = int(input("Dime cantidad de respuestas incorrectas:"))
puntos = respuestas_correctas * 5 + respuestas_incorrectas * (-1)
print("Puntos:",puntos)
