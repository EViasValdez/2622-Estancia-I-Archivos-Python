class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range (numero)]
    def IngresarDato (self):
        self.datos = [int(input("Ingresar dato " + str(i + 1)+": ")) for i in range(self.n)]
class Operaciones (Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)
    def Suma(self):
        a, b, = self.datos
        s = a + b
        print (f"El restultado es: {s}")
    def Resta(self):
        a, b, = self.datos
        r = a - b
        print (f"El restultado es: {r}")
    def Multiplicacion(self):
        a, b, = self.datos
        m = a * b
        print (f"El restultado es: {m}")
    def Division(self):
        a, b, = self.datos
        d = a / b
        print (f"El restultado es: {d}")

class Raiz (Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    def Cuadrada(self):
        import math
        a, = self.datos
        print (f"El resultado es: {math.sqrt(a)}")

objeto = Operaciones()
print(isinstance(objeto, Operaciones))
print(isinstance(objeto, Raiz))
print()

print(issubclass(Operaciones, Calculadora))
print(issubclass(Calculadora, Operaciones))