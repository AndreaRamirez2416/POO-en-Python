from abc import ABC, abstractmethod


class Cuenta(ABC):
    def __init__(self, NumeroCuenta, Saldo):
        self.NumeroCuenta = NumeroCuenta
        self.Saldo = Saldo
    
    @abstractmethod
    def consultar_saldo(self):
        print(self.Saldo)

    def Retirar(self, cantidad):
        if self.Saldo < cantidad:
            print("Saldo insuficiente")
        else:
            self.Saldo -= cantidad

    def Depositar(self, cantidad):
        self.Saldo += cantidad

class CuentaNomina(Cuenta):
    def __init__(self, NumeroCuenta, Saldo, Intereses):
        super().__init__(NumeroCuenta, Saldo)
        self.Intereses = Intereses
    
    def calcular_intereses(self):
        return self.Saldo * self.Intereses

    def consultar_saldo(self):
        print("Saldo actual: ", self.Saldo)

class CuentaAhorro(Cuenta):
    def __init__(self, NumeroCuenta, Saldo, Comision):
        super().__init__(NumeroCuenta, Saldo)
        self.Comision = Comision

    def calcular_intereses(self):
        return self.Saldo * self.Comision

    def consultar_saldo(self):
        print("Saldo actual: ", self.Saldo)

class CuentaCorriente(Cuenta):
    def __init__(self, NumeroCuenta, Saldo, Sobregiro):
        super().__init__(NumeroCuenta, Saldo)
        self.Sobregiro = Sobregiro

    def consultar_saldo(self):
        print("Saldo actual: ", self.Saldo)

    def calcular_intereses(self):
        return self.Saldo * self.Intereses

cuenta1 = CuentaNomina("123456789", 1000, 0.05)
cuenta1.consultar_saldo()
cuenta1 = CuentaAhorro("987654321", 2000, 0.02)
cuenta1.consultar_saldo()
cuenta1 = CuentaCorriente("456789123", 500, 1000)
cuenta1.consultar_saldo()