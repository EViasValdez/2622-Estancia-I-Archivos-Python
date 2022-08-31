class Estudiante:
    def __init__(self, nombre, apellido, edad, municipio):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.municipio = municipio

    def __str__(self):
        return f"Hola mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años y vivo en {self.municipio}"

    def __repr__(self):
        return f"Hola mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años y vivo en {self.municipio}"

EstudianteNuevo = Estudiante ("Eduardo", "Viñas", "22", "Tecamac")

print(f"{EstudianteNuevo}")
print(f"{EstudianteNuevo !r}")
