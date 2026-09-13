class Paciente:
    def __init__(self,nombre,edad,documento,telefono):
        self.nombre=nombre
        self.edad=edad
        self.documento=documento
        self.telefono=telefono
    def imprimir(self):
        print(f"nombre: {self.nombre}, edad: {self.edad}, documento: {self.documento}, telefono: {self.telefono}")
Paciente1=Paciente("juan", 30, 123456789, 3001234567)
Paciente2=Paciente("maria", 25, 987654321, 3009876543)

Paciente1.imprimir()
Paciente2.imprimir()
