print("----BIENVENIDO----")
print("---- 'CURVA LOCA' ----")
print("---- COMPAÑIA DE AUTOBUSES ----")
print("---- PRESIONE PARA CONTINUAR ----")
input()
print("PRECIO POR KILOMETRO:")
print("$20")
input()
Kilometro = int(input("Ingrese los kilómetros a viajar: "))
Precio = int(input("Ingrese el precio del kilómetro: "))
Total = Kilometro * Precio

print("El costo de su boleto por " + str(Kilometro) + " km es de $" + str(Total) + " pesos")