class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(10, 4)
print(operacion.suma)
print(operacion.resta)
print(operacion.multiplicacion)
print(operacion.division)