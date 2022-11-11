nombre = input ("Nombre completo: " )
materias = 5
contador = 1 
sumatoria = 0

while contador <= materias:
     nombre_materia = input("Ingresa el nombre de la (" + str(contador) + ") materia: ")
     calificacion = float(input ("calificacion obtenidas en " + str(nombre_materia) + ": "))

sumatoria = sumatoria + calificacion 
contador = contador + 1

promedio = sumatoria / materias
print ("__RESULTADOS__")
print (f"Hola, {nombre} tienes un promedio de {promedio} en el 5to semestre.")