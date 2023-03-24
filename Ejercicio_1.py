class libro:
    def describir_libro(self):
        self.titulo = input("Introduce el titulo del libro: ")
        self.autor = input("Introduce el autor del libro: ")
        self.paginas = int(input("Número de páginas del libro: "))
        self.precio = int(input("Precio del libro: "))
    def mostrar_libro(self):
        print("Titulo: ", self.titulo)
        print("Autor: ", self.autor)
        print("Páginas: ", self.paginas)
        print("Precio: ", self.precio)