#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha
#calificación se compone de los siguientes porcentajes:
#•55% del promedio de sus tres calificaciones parciales.
#•30% de la calificación del examen final.
#•15% de la calificación de un trabajo final.

primer_parcial = float(input("Dime la nota del primer parcial :"))
segundo_parcial= float(input("Dime la nota del segundo parcial :"))
tercer_parcial = float(input("Dime la nota del tercero parcial :"))
examen = float(input("Dime la nota del examen:"))
trabajo = float(input("Dime la nota del trabajo:"))
nota = ((primer_parcial + segundo_parcial + tercer_parcial) / 3) * 0.55 + 0.3 * examen + 0.15 * trabajo
print("Su nota final es :", nota)
