print("Determina el salario de un trabajador")
input()

Salario = 1500

for i in range (1, 7):
    Incremento = Salario * 0.10
    Salario = Salario + Incremento
    print("El salario en el año", i, "es de $" + str(Salario) + " pesos")
    i += 1

print("Al cabo de 6 años el salario es de $" + str(Salario) + " pesos")