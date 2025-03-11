# Polimorfismo con función.
class Tomate:
    def tipo(self):
        print("Es un vegetal")
    def color(self):
        print("Es de color rojo")
class Manzana:
    def tipo(self):
        print("Es una fruta")
    def color(self):
        print("Es de color verde")
def Funcion (objeto):
    objeto.tipo()
    objeto.color()
NuevoTomate = Tomate
print (Funcion(NuevoTomate()))
NuevaManzana = Manzana
print(Funcion(NuevaManzana()))

# Polimorfismo con métodos.
class Colombia:
    def Capital(self):
        print(" La capital es Bogotá")
    def Idioma(self):
        print("Es español")
class Francia:
    def Capital(self):
        print(" La capital es Paris")
    def Idioma(self):
        print("Es francés")
Colombiano = Colombia() # 1 Objeto.
Frances = Francia() # 2 Objeto.
for Pais in (Colombiano, Frances):
    print(Pais.Capital())
    print(Pais.Idioma())

# Polimorfismo con herencia.
class Aves:
    def Volar(self):
        print("La mayoría de aves pueden volar")
class Aguila(Aves):
    def Volar(self):
        print("Las águilas pueden volar")
class Gallina(Aves):
    def Volar(self):
        print("Las gallinas no pueden volar")
ObjAves = Aves()
ObjAguila = Aguila()
ObjGallina = Gallina()
print(ObjAves.Volar())
print(ObjAguila.Volar())
print(ObjGallina.Volar())