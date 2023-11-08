print("Promedio de un estudiante")
input()

print("Ponderaciones")
print("Primer examen = 25%")
print("Segundo examen = 25%")
print("Tercer examen = 50%")
input()

Examen1 = int(input("Ingrese el valor del primer examen: "))
Examen2 = int(input("Ingrese el valor del segundo examen: "))
Examen3 = int(input("Ingrese el valor del tercer examen: "))
Calificacion1 = Examen1 * 0.25
Calificacion2 = Examen2 * 0.25
Calificacion3 = Examen3 * 0.5
Promedio = (Calificacion1 + Calificacion2 + Calificacion3) / 3

print("El promedio del alumno es de: " + str(Promedio))