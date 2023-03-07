# Polimorfismo con funcion.
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

# Polimorfismo con metodos.
class Colombia:
    def Capital(self):
        print(" La capital es Bogota")
    def Idioma(self):
        print("Es español")
class Francia:
    def Capital(self):
        print(" La capital es Paris")
    def Idioma(self):
        print("Es frances")
Colombiano = Colombia() # 1 Objeto.
Frances = Francia() # 2 Objeto.
for pais in (Colombiano, Frances):
    print(pais.Capital())
    print(pais.Idioma())

# Polimorfismo con herencia.
class Aves:
    def volar(self):
        print("La mayoria de aves pueden volar")
class Aguila(Aves):
    def volar(self):
        print("Las aguilas pueden volar")
class Gallina(Aves):
    def volar(self):
        print("Las gallinas no pueden volar")
ObjAves = Aves()
ObjAguila = Aguila()
ObjGallina = Gallina()
print(ObjAves.volar())
print(ObjAguila.volar())
print(ObjGallina.volar())