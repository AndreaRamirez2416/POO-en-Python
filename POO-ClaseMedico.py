class Medico:
    def __init__(self,nombre,espepecialidad,tarjeta_profecional):
        self.nombre=nombre
        self.especialidad=espepecialidad
        self.tarjeta_profecional=tarjeta_profecional

    def imprimir(self):
        print(f"nombre: {self.nombre}, especialidad: {self.especialidad}, tarjeta_profecional: {self.tarjeta_profecional}")
Medico1=Medico("dr. juan", "cardiología", "12345")
Medico2=Medico("dra. maría", "neurología", "67890")

Medico1.imprimir()
Medico2.imprimir()
