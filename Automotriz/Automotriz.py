print("==== Automotriz Calarin ====")
input()

print("Clave del vehículo")
print("Indicar la clave del vehículo (1, 2, 3): ")
Clave = int(input())
print("Cantidad de carros a calcular el porcentaje")
Cantidad = int(input())
print("Precio bruto del lote de vehículos")
Precio = int(input())

Uno = 1 + 0.10
Dos = 0.7 / 100
Tres = 0.5

if Clave == 1:
    Imp1 = Clave * Precio

if Clave == 2:
    Imp2 = (1 + Dos)

if Clave == 3:
    Imp3 = (1 + Tres) / 100

Resultado = Clave * Precio

print("Clave elegida ", Clave, "Cantidad de ", Cantidad, "autos", "Costo total ", Precio)
print("El % a pagar de los valores ingresados son: ", Resultado)