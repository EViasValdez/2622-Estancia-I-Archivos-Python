print("++++ COMPAÑIA TELEFONICA ++++")
print("++++ CUATRO PESOS POR MINUTO ++++")
input()
Minutos = int(input("Ingrese los minutos de la llamada: "))
Precio = int(input("Ingrese el precio por minutos de la llamada: "))
Total = Minutos * Precio

print("El costo de su llamada por " + str(Minutos) + " minutos es de $" + str(Total) + " pesos")