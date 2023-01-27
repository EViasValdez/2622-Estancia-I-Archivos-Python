class Persona:
    def __init_(self):
        self.Nombre = input("Ingrese el nombre: ")
        self.Edad = int(input("Ingrese la edad: "))
    def imprimir(self):
        print("Nombre: ", self.Nombre)
        print("Edad: ",  self.Edad)
class Ciudadano(Persona):
    def __init__(self):
        super().__init__()
        self.Deposito = float(input("Ingrese el dinero a depositar: "))
    def imprimir(self):
        super().imprimir()
        print("Deposito: ", self.Deposito)
    def inpuestos(self):
        if self.Deposito > 4000:
            print(f"El ciudadano {self.Nombre} debe pagar impuestos")
        else:
            print(f"El ciudadano {self.Nombre} no debe pagar impuestos")

Cuidadano1 = Ciudadano()
Cuidadano1.imprimir()
Cuidadano1.impuestos()