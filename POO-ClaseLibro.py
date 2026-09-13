class Libro:
    def __init__(self,titulo,autor,año,categoria):
        self.titulo=titulo
        self.autor=autor
        self.año=año
        self.categoria=categoria
    def imprimir(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Categoria: {self.categoria}")
Libro1=Libro("El principito", "Antoine de Saint-Exupéry", 1943, "Fábula")
Libro2=Libro("1984", "George Orwell", 1948, "Distopía")

Libro1.imprimir()