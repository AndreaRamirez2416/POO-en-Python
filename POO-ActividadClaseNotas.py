class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def calcular_promedio(self):
        suma = sum(self.notas)
        promedio = suma / len(self.notas)
        return promedio

    def validar_aprobacion(self):
       for promedio in self.notas:
            if promedio < 3.0:
                return "Reprobado"
            return "Aprobado"

ListaEstudiantes = []
E1 = Estudiante("Juan", [4.0, 3.5, 2.8, 4.5])
E2 = Estudiante("Maria", [3.0, 3.2, 3.8, 4.0])
E3 = Estudiante("Pedro", [2.5, 2.8, 3.0, 3.5])
ListaEstudiantes.append(E1)
ListaEstudiantes.append(E2)
ListaEstudiantes.append(E3)
for estudiante in ListaEstudiantes:
    print(f"Promedio de {estudiante.nombre}: {estudiante.calcular_promedio()} - Estado: {estudiante.validar_aprobacion()}")