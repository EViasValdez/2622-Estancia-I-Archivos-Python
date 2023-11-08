class Televisor:
    Tipo = "Grande"
    Marca = "Hisense"

TV = Televisor()
print("La marca de este televisor es", TV.Marca)
print("La marca de este televisor es", getattr(TV, "marca"))
print("¿La pantalla es grande?", hasattr(TV, "Tipo"))

print("Antes era", TV.Marca)
setattr(TV, "marca", "Sony")
print("Ahora es", TV.Marca)