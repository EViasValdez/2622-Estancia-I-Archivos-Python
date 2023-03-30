class Telefono:
    def __init__(self):
        pass
    def Llamar(self):
        print("Llamando....")
    def Ocupado(self):
        print("Ocupado....")
class Camara:
    def __init__(self):
        pass
    def Fotografia(self):
        print("Tomando fotos....")
class Reproduccion:
    def __init__(self):
        pass
    def ReproduccionVideo(self):
        print("Reproduciendo video....")
    def ReproduccionMusica(self):
        print("Reproduciendo musica...")
class TelefonoCelular (Telefono, Camara, Reproduccion):
    def __del__(self):
        print("Telefono apagado...")

Celular = TelefonoCelular()
Repr = Reproduccion()

print(Celular.Fotografia())
print(Celular.Llamar())
print(Repr.ReproduccionVideo())
print(Repr.ReproduccionMusica())