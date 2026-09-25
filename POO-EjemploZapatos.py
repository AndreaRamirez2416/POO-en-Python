class Zapatos:
    def __init__(self, estilo, marca, talla, color):
        self.estilo = estilo
        self.marca = marca
        self.talla = talla
        self.color = color

    def mostrar_informacion(self):
        print(f"Estilo: {self.estilo}, Marca: {self.marca}, Talla: {self.talla}, Color: {self.color}") 

    def disponibilidad(self):
        print(f"Los {self.estilo} de la marca {self.marca} en talla {self.talla} y color {self.color} están disponibles.")

    def visibilidad(self):
        print(f"Los {self.estilo} de la marca {self.marca} en talla {self.talla} y color {self.color} son visibles.")

Botines = Zapatos("Botines", "Nike", 42, "Negro")
Botines.mostrar_informacion()
Botines.disponibilidad()
Botines.visibilidad()