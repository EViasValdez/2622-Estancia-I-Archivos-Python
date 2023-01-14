class Televisor:
    Tipo = "Grande"
    marca = "Hisense"

TV = Televisor()
print("La marca de este televisor es", TV.marca)
print("La marca de este televisor es", getattr(TV, "marca"))
print("¿La pantalla es grande?", hasattr(TV, "Tipo"))

print("Antes era", TV.marca)
setattr(TV, "marca", "Sony")
print("Ahora es", TV.marca)