# Factoriales.
def Factorial(Numero):
    Resultado = 1

    for i in range(Numero - 1, 2, - 1):
        Resultado = Resultado * i
    return Resultado
print(Factorial(5))

# Numeros enteros.
def NumeroSen(N1, N2):
    if (N1 > N2):
        Aux = N1
        N1 = N2
        N2 = Aux
    
    for i in range(N1 + 1, N2):
        print(i)

NumeroSen(1, 100)