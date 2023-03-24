class Animal:
    def __init__(self, especie, tipo):
        self.especie = especie
        self.tipo = tipo
    def mostrar_animal(self):
        print("Animal: ", self.especie, ", Tipo: ", self.tipo)

animal1 = Animal("Pollo", "No se dice", "Ovíparo")
animal2 = Animal("Ornitorrinco", "Mamífero", "Ovíparo")
animal3 = Animal("Gato", "Mamífero", "No se dice")
animal1.mostrar_animal()
animal2.mostrar_animal()
animal3.mostrar_animal()