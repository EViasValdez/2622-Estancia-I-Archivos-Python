class Figura:
    def __init__(self,nombre):
        self.nombre = nombre
    def tipo_figura(self):
        pass
class Esfera (Figura):
    def tipo_figura(self):
        print("Circulo")
class Cubo (Figura):
    def tipo_figura(self):
       print("Cuadrado")
NuevaFigura1 = Esfera ("Circular")
print(NuevaFigura1.tipo_figura())
print(NuevaFigura1.nombre)

NuevaFigura2 = Cubo ("Cubica")
print(NuevaFigura2.tipo_figura())
print(NuevaFigura2.nombre)