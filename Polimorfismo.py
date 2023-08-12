class Figura:
    def __init__(self, nombre):
        self.Nombre = Nombre
    def TipoFigura(self):
        pass
class Esfera (Figura):
    def TipoFigura(self):
        print("Circulo")
class Cubo (Figura):
    def TipoFigura(self):
       print("Cuadrado")
NuevaFigura1 = Esfera ("Circular")
print(NuevaFigura1.TipoFigura())
print(NuevaFigura1.Nombre)

NuevaFigura2 = Cubo ("Cubica")
print(NuevaFigura2.TipoFigura())
print(NuevaFigura2.Nombre)