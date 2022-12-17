Nombre = input ("Nombre completo: " )
Materias = 5
Contador = 1 
Sumatoria = 0

while Contador <= Materias:
     nombre_materia = input("Ingresa el nombre de la (" + str(Contador) + ") materia: ")
     calificacion = float(input ("calificacion obtenidas en " + str(NombreMateria) + ": "))

Sumatoria = Sumatoria + calificacion 
Contador = Contador + 1

Promedio = Sumatoria / Materias
print ("__RESULTADOS__")
print (f"Hola, {Nombre} tienes un promedio de {Promedio} en el 5to semestre.")