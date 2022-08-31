# Factoriales
def factorial(numero):
    resultado = 1

    for i in range(numero - 1, 2, - 1):
        resultado = resultado * i
    return resultado
print(factorial(5))

# Numeros enteros
def numerosen(n1, n2):
    if (n1 > n2):
        aux = n1
        n1 = n2
        n2 = aux
    
    for i in range(n1 + 1, n2):
        print(i)

numerosen(1, 100)
    
