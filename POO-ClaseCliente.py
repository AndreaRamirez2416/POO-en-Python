class Cliente:
    def __init__(self,nombre,telefono,direccion):
        self.nombre=nombre
        self.telefono=telefono
        self.direccion=direccion
    def imprimir(self):
        print(f"nombre: {self.nombre}, telefono: {self.telefono}, direccion: {self.direccion}")
Cliente1=Cliente("erika peña",3104965696,"cra 1b # 9-45")
Cliente2=Cliente("ligia moscoso", 3213296309, "cll 9t # 10-56")

Cliente1.imprimir()
Cliente2.imprimir()
Cliente1.nombre="andrea"
Cliente1.imprimir()