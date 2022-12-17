class Calculadora:
    def __init__(self, n1, n2):
        self.Suma = n1 + n2
        self.Resta = n1 - n2
        self.Multiplicacion = n1 * n2
        self.Division = n1 / n2

Operacion = Calculadora(10, 4)
print(Operacion.Suma)
print(Operacion.Resta)
print(Operacion.Multiplicacion)
print(Operacion.Division)