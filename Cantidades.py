def Cantidades():
    Lista = []
    X = 1
    A = 0
    B = 0
    C = 0

    Nums = int (input("Ingrese los numeros a ingresar:  "))

    while X <= Nums:
        N = int (input ("Introduzca numero " + str(X) + ": "))
        Lista.append(N)
        if N < 0:
            A = A + 1
        else:
            if N == 0:
                C = C + 1
            else:
                C = C + 1
        
        X = X + 1

    print("Los numeros introducidos son: ", Lista)
    print("Las cantidades menores a cero son: " + str(A))
    print("Las cantidades iguales a cero son: " + str(B))
    print("Las cantidades mayores a cero son: " + str(C))

Cantidades()