# Metodo constructor
class Cubo:
    pass
    def __init__(self, bidimensional, lados):
        self.bidimensional = bidimensional
        self.lados = lados
    def desc(self):
        return "{} tiene {}".format(self.bidimensional, self.lados)
    def comentario(self, texto):
        return "{} he aqui un texto {}".format(self.bidimensional, texto)
        
figura = Cubo("Si", "4")
print(figura.desc())
print(figura.comentario("¿Que paso?"))

# Modificacion de un atributo
class Rombo:
    def __init__(self):
        self.la = False
    def enviar_rombo(self):
        self.en = True

figu = Rombo()

print(figu.en)
figu.enviar_rombo()
print(figu.en)
