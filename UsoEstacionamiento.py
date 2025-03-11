print("Determinar el precio a pagar por el uso del estacionamiento")
input()

Hora = int(input("Ingrese el número de horas: "))
Total = 0.0

if Hora <= 2:
    Total = Hora * 5
elif Hora <= 5:
    Total = ((Hora - 2) * 4) + 10
elif Hora <= 10:
    Total = ((Hora - 5) * 3) + 22
else:
    Total = ((Hora - 10) * 2) + 37
print("El total a pagar de " + str(Hora) + " es de: $" + str(Total) + " pesos")