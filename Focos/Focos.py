print("")
print("")
print("---- Pfic ----")
print("---- Fabrica de focos ----")
input()

def FabricaFocos():
    F = 1
    V = 0
    B = 0
    R = 0 
    C = int(input("Ingrese cantidad de focos: "))

    while F <= C:
        N = int(input ("Eliga el color \n 1 - Rojo \n 2 - Amarillo \n 3 - Azul \n"))
        
        if N == 1:
            V = V + 1
        else:
            if N == 2:
                B = B + 1
            else:
                R = R + 1
        F = F + 1

    print("El total de focos rojos es: " + str(V))
    print("El total de focos amarillos es: " + str(B))
    print("El total de focos azules es: " + str(R))
FabricaFocos()