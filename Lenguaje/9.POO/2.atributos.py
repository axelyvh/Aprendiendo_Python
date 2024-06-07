class Perro:

    # Atributo de clase
    especie = "mamifero"

    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza


mi_perro = Perro("Roly", "Max")
print(type(mi_perro))
print(mi_perro.nombre)
print(mi_perro.raza)