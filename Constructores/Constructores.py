# Método constructor.
class Cubo:
    pass
    def __init__(self, Bidimensional, Lados):
        self.Bidimensional = Bidimensional
        self.Lados = Lados
    def Desc(self):
        return "{} tiene {}".format(self.Bidimensional, self.Lados)
    def Comentario(self, Texto):
        return "{} he aquí un texto {}".format(self.Bidimensional, Texto)

Figura = Cubo("Si", "4")
print(Figura.Desc())
print(Figura.Comentario("¿Que paso?"))

# Modificación de un atributo ".await".
class Rombo:
    def __init__(self):
        self.la = False
    def EnviarRombo(self):
        self.En = True

Figu = Rombo()
print(Figu.En)
Figu.EnviarRombo()
print(Figu.En)