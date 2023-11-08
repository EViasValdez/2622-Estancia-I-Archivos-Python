class Calculadora:
    def __init__(self, N1, N2):
        self.Suma = N1 + N2
        self.Resta = N1 - N2
        self.Multiplicacion = N1 * N2
        self.Division = N1 / N2

Operacion = Calculadora(10, 4)
print(Operacion.Suma)
print(Operacion.Resta)
print(Operacion.Multiplicacion)
print(Operacion.Division)