def Ahorro():
    Centavos = 3
    D = 1

    while D <= 365:
        Centavos = Centavos * 3

        if Centavos <= 100:
            print("Dia " + str(D) + ": $" + str(Centavos) + " centavos")
        else:
            print("Dia " + str(D) + ": $" + str(Centavos) + " pesos")
        
        D = D + 1

    print("El ahorro es de: $" + str(Centavos) + " pesos")

Ahorro()
