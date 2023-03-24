class libro:
    def describir_libro(self):
        self.titulo = input("Introduce el titulo del libro: ")
        self.autor = input("Introduce el autor del libro: ")
        self.paginas = int(input("Número de páginas del libro: "))