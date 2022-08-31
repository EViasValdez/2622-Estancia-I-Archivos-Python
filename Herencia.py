class Figura:
    pass
    def __init__(self,nombre, tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return "{} es una figura de tipo {}".format(self.nombre, self.tipo)

class cubo(Figura):
    def detalles(self, tipodetalles):
        return "{} tiene cuatro lados {}".format(self.nombre, tipodetalles)

class circulo(Figura):
    def detalles(self, tipodetalles):
        return "{} tiene cuatro lados {}".format(self.nombre, tipodetalles)

objeto_nuevo = cubo("Cubo","Electrico")
print(objeto_nuevo.descripcion())
print(objeto_nuevo.detalles("Cubico"))
