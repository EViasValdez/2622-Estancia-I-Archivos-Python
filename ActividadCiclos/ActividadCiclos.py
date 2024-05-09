Nombre = input("Nombre completo: ")
Materias = 5
Contador = 1 
Sumatoria = 0

while Contador <= Materias:
     NombreMateria = input("Ingresa el nombre de la (" + str(Contador) + ") materia: ")
     Calificacion = float(input ("calificacion obtenida en " + str(NombreMateria) + ": "))

Sumatoria = Sumatoria + Calificacion 
Contador = Contador + 1

Promedio = Sumatoria / Materias
print ("____RESULTADOS____")
print (f"Hola, {Nombre} tienes un promedio de {Promedio} en el 5to semestre.")