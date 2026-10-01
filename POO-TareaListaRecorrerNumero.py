class ListaDeNumeros:
    def __init__(self):
        self.numeros = []

    def agregar_numero(self, numero):
        self.numeros.append(numero)

    def recorrer_numeros(self):
        for numero in self.numeros:
            print(numero)

    def mostrar(self):
        print("mayor:", max(self.numeros))
        print("menor:", min(self.numeros))
        print("promedio:", sum(self.numeros) / len(self.numeros))

datos = ListaDeNumeros()
cantidad = int(input("Ingrese la cantidad de números que desea agregar: "))
for _ in range(cantidad):
    numero = int(input("Ingrese un número: "))
    datos.agregar_numero(numero)

datos.recorrer_numeros()
datos.mostrar()