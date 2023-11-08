class Pastel:
    def __init__(self, Ingredientes):
        self.Ingredientes = Ingredientes
    def __repr__(self):
        return f"Pastel {self.Ingredientes !r}"
    @classmethod
    def PastelChocolate(cls):
        return cls(["Harina","Leche","Chocolate"])
    @classmethod
    def PastelVainilla(cls):
        return cls(["Harina","Leche","Vainilla"])
print(Pastel.PastelChocolate())
print(Pastel.PastelVainilla())

import Math
class Pastel:
    def __init__(self, Ingredientes, Tamaño):
        self.Ingredientes = Ingredientes
        self.Tamaño = Tamaño
    def __repr__(self):
        return f"Pastel {self.Ingredientes} " f"{self.Tamaño}"
    def area(self):
        return self.TamañoArea (self.Tamaño)
    @staticmethod
    def TamañoArea(A):
        return A **2* Math.pi
NuevoPastel = Pastel(["Harina", "Azucar", "Leche", "Crema"], 4)

print(NuevoPastel.Ingredientes)
print(NuevoPastel.Tamaño)
print(NuevoPastel.TamañoArea(20))