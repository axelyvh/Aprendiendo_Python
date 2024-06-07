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


class Perro(Animal):
    def hablar(self):
        print("Guau")

    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muu!")

    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzz!")

    def moverse(self):
        print("Volando")

    # Nuevo metodo
    def picar(self):
        print("Picar!")

print(Perro.__bases__)
print(Animal.__subclasses__())

mi_perro = Perro("Mamifero", 10)
mi_vaca = Vaca("Mamifero", 23)
mi_abeja = Abeja("Insecto", 1)

mi_perro.hablar()
mi_vaca.hablar()

mi_vaca.describeme()
mi_abeja.describeme()

mi_abeja.picar()