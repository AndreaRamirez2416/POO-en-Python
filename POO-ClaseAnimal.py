class Animal:
    def __init__(self,nombre, color, especie):
        self.nombre=nombre
        self.color=color
        self.especie=especie
    def hacer_sonido(self):
        return ("este animal hace un sonido")
    def presentarse(self):
        return (f"hola soy {self.nombre}, soy un {self.especie} y mi color es {self.color}")

class Perro(Animal):
    def __init__(self,nombre, color, especie, raza):
        super().__init__(nombre, color, especie)
        self.raza=raza
    def hacer_sonido(self):
        return ("guau guau")
    def buscar_pelota(self):
        return (f"{self.nombre} esta buscando la pelota")
    
class Gato(Animal):
    def __init__(self,nombre, color, especie, raza):
        super().__init__(nombre, color, especie)
        self.raza=raza
    def hacer_sonido(self):
        return ("miau miau")
    def trepar_arbol(self):
        return (f"{self.nombre} esta trepando un arbol")
    def cazar_raton(self):
        return (f"{self.nombre} esta cazando un raton")

Animal1=Perro("Firulais", "marron", "perro", "labrador")
Animal2=Gato("Michi", "blanco", "gato", "siames")

print(Animal1.presentarse())
print(Animal2.presentarse())
print(Animal1.hacer_sonido())
print(Animal2.hacer_sonido())
print(Animal1.buscar_pelota())
print(Animal2.trepar_arbol())
print(Animal2.cazar_raton())