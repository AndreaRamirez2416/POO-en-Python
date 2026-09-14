class Cuenta_Banco:
    def __init__(self, titular, saldo=0, documento=None):
        self.titular = titular
        self.saldo = saldo
        self.documento = documento

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return(f"Depósito exitoso: {cantidad}. Saldo actual: {self.saldo}")
        else:
            return("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return(f"Retiro exitoso: {cantidad}. Saldo actual: {self.saldo}")
        else:
            return("Cantidad inválida o saldo insuficiente.")

    def mostrar_saldo(self):
        return(f"Titular: {self.titular}, Saldo actual: {self.saldo}")

class Cuenta_Ahorro(Cuenta_Banco):
    def __init__(self, titular, saldo=0, documento=None, tasa_interes=0.01):
        super().__init__(titular, saldo, documento)
        self.tasa_interes = tasa_interes

    def calcular_interes(self):
        interes = self.saldo * self.tasa_interes
        return(f"Interés generado: {interes}")

    def mostrar_saldo(self):
        super().mostrar_saldo()
        return(f"Tasa de interés: {self.tasa_interes * 100}%")

    def presentar_cuenta(self):
        return(f"Cuenta de Ahorro - Titular: {self.titular}, Saldo: {self.saldo}, Documento: {self.documento}, Tasa de interés: {self.tasa_interes * 100}%")
    
class Cuenta_Corriente(Cuenta_Banco):
    def __init__(self, titular, saldo=0, documento=None, limite_descubierto=1000):
        super().__init__(titular, saldo, documento)
        self.limite_descubierto = limite_descubierto

    def retirar(self, cantidad):
        if 0 < cantidad <= (self.saldo + self.limite_descubierto):
            self.saldo -= cantidad
            return(f"Retiro exitoso: {cantidad}. Saldo actual: {self.saldo}")
        else:
            return("Cantidad inválida o excede el límite de descubierto.")

    def mostrar_saldo(self):
        super().mostrar_saldo()
        return(f"Límite de descubierto: {self.limite_descubierto}")

    def presentar_cuenta(self):
        return(f"Cuenta Corriente - Titular: {self.titular}, Saldo: {self.saldo}, Documento: {self.documento}, Límite de descubierto: {self.limite_descubierto}")

Cuenta_Banco1 = Cuenta_Ahorro("Juan Perez", 1000, "12345678", 0.02)
Cuenta_Banco2 = Cuenta_Corriente("Maria Lopez", 500, "87654321", 2000)
print(Cuenta_Banco1.presentar_cuenta())
print(Cuenta_Banco1.depositar(200))
print(Cuenta_Banco1.mostrar_saldo())
print(Cuenta_Banco1.calcular_interes())
print(Cuenta_Banco2.presentar_cuenta())
print(Cuenta_Banco2.retirar(600))
print(Cuenta_Banco2.mostrar_saldo())
