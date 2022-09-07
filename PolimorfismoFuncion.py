# Polimorfismo con funcion
class Tomate:
    def tipo(self):
        print("Es un vejetal")
    def color(self):
        print("Es de colo rojo")
class Manzana:
    def tipo(self):
        print("Es una fruta")
    def color(self):
        print("Es de colo verde")
def funcion (objeto):
    objeto.tipo()
    objeto.color()
nuevo_tomate = Tomate
print (funcion(nuevo_tomate()))
nuevo_manzana = Manzana
print(funcion(nuevo_manzana()))

# Polimorfismo con metodos
class Colombia:
    def capital(self):
        print(" La capital es Bogota")
    def idioma(self):
        print("Es español")
class Francia:
    def capital(self):
        print(" La capital es Paris")
    def idioma(self):
        print("Es frances")
Colombiano = Colombia() # 1 Objeto
Frances = Francia() # 2 Objeto
for pais in (Colombiano, Frances):
    print(pais.capital())
    print(pais.idioma())

# Polimorfismo con herencia
class Aves:
    def volar(self):
        print("La mayoria de aves pueden volar")
class Aguila(Aves):
    def volar(self):
        print("Las aguilas pueden volar")
class Gallina(Aves):
    def volar(self):
        print("Las gallinas no pueden volar")
obj_Aves = Aves()
obj_Aguila = Aguila()
Obj_gallina = Gallina()
print(obj_Aves.volar())
print(obj_Aguila.volar())
print(Obj_gallina.volar())