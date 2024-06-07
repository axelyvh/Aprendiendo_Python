class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un animal de tipo", type(self).__name__)

class Mamifero(Animal):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)

class Perro(Mamifero):

    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        self.dueño = dueño

    def hablar(self):
        print("Guau")

    def moverse(self):
        print("Caminando con 4 patas")

mi_perro = Perro("Mestizo", "5", "Axel")
mi_perro.describeme()
print(mi_perro.especie)