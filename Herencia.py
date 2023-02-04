class Figura:
    pass
    def __init__(self, Nombre, Tipo) -> None:
        self.Nombre = Nombre
        self.Tipo = Tipo
    def descripcion(self):
        return "{} es una figura de Tipo {}".format(self.Nombre, self.Tipo)

class cubo(Figura):
    def detalles(self, TipoDetalles):
        return "{} tiene cuatro lados {}".format(self.Nombre, TipoDetalles)

class circulo(Figura):
    def detalles(self, TipoDetalles):
        return "{} tiene cuatro lados {}".format(self.Nombre, TipoDetalles)

ObjetoNuevo = cubo("Cubo","Electrico")
print(ObjetoNuevo.descripcion())
print(ObjetoNuevo.detalles("Cubico"))