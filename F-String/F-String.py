class Estudiante:
    def __init__(self, Nombre, Apellido, Edad, Municipio):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.Municipio = Municipio
    def __str__(self):
        return f"Hola mi nombre es {self.Nombre} {self.Apellido}, tengo {self.Edad} años y vivo en {self.Municipio}"

    def __repr__(self):
        return f"Hola mi nombre es {self.Nombre} {self.Apellido}, tengo {self.Edad} años y vivo en {self.Municipio}"

EstudianteNuevo = Estudiante("Eduardo", "Viñas", "22", "Tecamac")

print(f"{EstudianteNuevo}")
print(f"{EstudianteNuevo !r}")