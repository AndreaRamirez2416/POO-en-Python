class Ordenamiento:
    def __init__(self, Numeros):
        self.Numeros = Numeros

    def MetodoBurbuja(self):
        n = len(self.Numeros)
        for i in range(n): 
            for j in range(0, n-i-1):
                if self.Numeros[j] > self.Numeros[j+1]:
                    self.Numeros[j], self.Numeros[j+1] = self.Numeros[j+1], self.Numeros[j]

        return self.Numeros
Ordenar=Ordenamiento([64, 34, 25, 12, 22, 11, 90])
print(Ordenar.MetodoBurbuja())
