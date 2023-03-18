# Metodo constructor.
class Cubo:
    pass
    def __init__(self, Bidimensional, Lados):
        self.Bidimensional = Bidimensional
        self.Lados = Lados
    def desc(self):
        return "{} tiene {}".format(self.Bidimensional, self.Lados)
    def comentario(self, Texto):
        return "{} he aqui un texto {}".format(self.Bidimensional, Texto)

Figura = Cubo("Si", "4")
print(Figura.desc())
print(Figura.comentario("¿Que paso?"))

# Modificacion de un atributo ".await".
class Rombo:
    def __init__(self):
        self.la = False
    def enviar_rombo(self):
        self.En = True

Figu = Rombo()
print(Figu.En)
Figu.enviar_rombo()
print(Figu.En)