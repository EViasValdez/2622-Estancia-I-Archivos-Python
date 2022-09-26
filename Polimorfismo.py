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
nueva_figura = Esfera ("Circular")
print(nueva_figura.tipo_figura())
print(nueva_figura.nombre)

nueva_figura2 = Cubo ("Cubica")
print(nueva_figura2.tipo_figura())
print(nueva_figura2.nombre)
