class libro:
    def __init__(self):
        self.titulo = input("Introduce el titulo del libro: ")
        self.autor = input("Introduce el autor del libro: ")
        self.paginas = int(input("Número de páginas del libro: "))
        self.precio = int(input("Precio del libro: "))
    def mostrar_libro(self):
        print("Titulo: ", self.titulo)
        print("Autor: ", self.autor)
        print("Páginas: ", self.paginas)
        print("Precio: ", self.precio)
# def main():
#     libro1 = libro()
#     libro1.describir_libro()
#     libro1.mostrar_libro()
def main():
    libro1 = libro()
    libro1.mostrar_libro()
if __name__ == "__main__":
    main()