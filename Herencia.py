class Figura:
    pass
    def __init__(self, Nombre, Tipo) -> None:
        self.Nombre = Nombre
        self.Tipo = Tipo
    def Descripcion(self):
        return "{} es una figura de Tipo {}".format(self.Nombre, self.Tipo)

class Cubo(Figura):
    def Detalles(self, TipoDetalles):
        return "{} tiene cuatro lados {}".format(self.Nombre, TipoDetalles)

class circulo(Figura):
    def Detalles(self, TipoDetalles):
        return "{} tiene cuatro lados {}".format(self.Nombre, TipoDetalles)

ObjetoNuevo = Cubo("Cubo", "Electrico")
print(ObjetoNuevo.Descripcion())
print(ObjetoNuevo.Detalles("Cubico"))