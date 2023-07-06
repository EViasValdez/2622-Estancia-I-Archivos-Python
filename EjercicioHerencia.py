class Calculadora:
    def __init__(self, Numero):
        self.N = Numero
        self.Datos = [0 for i in range (Numero)]
    def IngresarDato (self):
        self.Datos = [int(input("Ingresar dato " + str(i + 1)+": ")) for i in range(self.n)]
class Operaciones (Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)
    def Suma(self):
        A, B, = self.Datos
        S = A + B
        print (f"El restultado es: {S}")
    def Resta(self):
        A, B, = self.Datos
        R = A - B
        print (f"El restultado es: {R}")
    def Multiplicacion(self):
        A, B, = self.Datos
        M = A * B
        print (f"El restultado es: {M}")
    def Division(self):
        A, B, = self.Datos
        D = A / B
        print (f"El restultado es: {D}")

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    def Cuadrada(self):
        import math
        A, = self.Datos
        print (f"El resultado es: {math.sqrt(A)}")

Objeto = Operaciones()
print(isinstance(Objeto, Operaciones))
print(isinstance(Objeto, Raiz))
print()

print(issubclass(Operaciones, Calculadora))
print(issubclass(Calculadora, Operaciones))