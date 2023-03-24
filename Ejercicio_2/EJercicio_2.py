class animal:
    def __init__(self, Pollo, Ornitorrinco, Gato):
        self.animal1 = input(Pollo)
        self.animal2 = input(Ornitorrinco)
        self.animal3 = input(Gato)
        self.tipo = input("Su tipo es ovíparo")
        self.especie = input("Su especie es mamífero")
        if Pollo:
            print("Es un animal ovíparo")
        elif Ornitorrinco:
            print("Es un animal mamífero y ovíparo")
        elif Gato:
            print("Es un animal mamífero")
    def mostrar_animal(self):
        print("Animal: ", self.animal1)
        print("Animal: ", self.animal2)
        print("Animal: ", self.animal3)

def main():
    print("Escoge un animal entre pollo, ornitorrinco y gato")