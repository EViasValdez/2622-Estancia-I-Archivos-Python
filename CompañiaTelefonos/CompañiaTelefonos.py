print("++++ COMPAÑIA TELEFONICA ++++")
print("++++ CUATRO PESOS POR MINUTO ++++")
input()

Minutos = int(input("Ingrese los minutos de la llamada: "))
Precio = int(input("Ingrese el precio por minutos de llamada: "))

Total = Minutos * Precio
print("El costo de su llamada por " + str(Minutos) + " minutos es de un total de $" + str(Total) + " pesos")