class Persona:
    def __init_(self):
        self.Nombre = input("Ingrese el nombre: ")
        self.Edad = int(input("Ingrese la edad: "))
    def Imprimir(self):
        print("Nombre: ", self.Nombre)
        print("Edad: ", self.Edad)
class Ciudadano(Persona):
    def __init__(self):
        super().__init__()
        self.Deposito = float(input("Ingrese el dinero a depositar: "))
    def Imprimir(self):
        super().imprimir()
        print("Deposito: ", self.Deposito)
    def Impuestos(self):
        if self.Deposito > 4000:
            print(f"El ciudadano {self.Nombre} debe pagar impuestos")
        else:
            print(f"El ciudadano {self.Nombre} no debe pagar impuestos")

Cuidadano1 = Ciudadano()
Cuidadano1.Imprimir()
Cuidadano1.Impuestos()