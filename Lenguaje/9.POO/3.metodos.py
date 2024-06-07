class Perro:

    # Atributo de clase
    especie = "mamifero"

    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

mi_perro = Perro("Roly", "Max")
mi_perro.ladra()
mi_perro.camina(10)