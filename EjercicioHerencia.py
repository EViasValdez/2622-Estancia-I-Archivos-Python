class Calculadora:
    def __init__(self, Numero):
        self.n = Numero
        self.Datos = [0 for i in range (Numero)]
    def IngresarDato (self):
        self.Datos = [int(input("Ingresar dato " + str(i + 1)+": ")) for i in range(self.n)]
class Operaciones (Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)
    def Suma(self):
        a, b, = self.Datos
        s = a + b
        print (f"El restultado es: {s}")
    def Resta(self):
        a, b, = self.Datos
        r = a - b
        print (f"El restultado es: {r}")
    def Multiplicacion(self):
        a, b, = self.Datos
        m = a * b
        print (f"El restultado es: {m}")
    def Division(self):
        a, b, = self.Datos
        d = a / b
        print (f"El restultado es: {d}")

class Raiz (Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    def Cuadrada(self):
        import math
        a, = self.Datos
        print (f"El resultado es: {math.sqrt(a)}")

Objeto = Operaciones()
print(isinstance(Objeto, Operaciones))
print(isinstance(Objeto, Raiz))
print()

print(issubclass(Operaciones, Calculadora))
print(issubclass(Calculadora, Operaciones))