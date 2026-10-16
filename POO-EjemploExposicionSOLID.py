
from abc import ABC, abstractmethod


# S - Principio de responsabilidad única
class Cuenta(ABC):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print("Deposito realizado correctamente.")

    @abstractmethod
    def retirar(self, cantidad):
        pass


# O - Principio abierto/cerrado
class CuentaAhorros(Cuenta):
    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False


class CuentaNomina(Cuenta):
    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False


# L - Principio de sustitucion de Liskov
def procesar_retiro(cuenta, cantidad):
    if cuenta.retirar(cantidad):
        print("Retiro exitoso:", cuenta.titular)
    else:
        print("Retiro rechazado:", cuenta.titular)


# I - Principio de segregacion de interfaces
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass


class NotificadorConsola(Notificador):
    def enviar(self, mensaje):
        print("NOTIFICACION:", mensaje)


# D - Principio de inversion de dependencias
class ServicioBancario:
    def __init__(self, notificador):
        self.notificador = notificador

    def realizar_retiro(self, cuenta, cantidad):
        if cuenta.retirar(cantidad):
            self.notificador.enviar(
                f"Retiro exitoso para {cuenta.titular}"
            )
        else:
            self.notificador.enviar(
                f"Retiro rechazado para {cuenta.titular}"
            )


# PROGRAMA PRINCIPAL
ahorros = CuentaAhorros("Ana", 100000)
nomina = CuentaNomina("Carlos", 200000)

notificador = NotificadorConsola()
servicio = ServicioBancario(notificador)

servicio.realizar_retiro(ahorros, 25000)
servicio.realizar_retiro(nomina, 50000)

print("Saldo de Ana:", ahorros.consultar_saldo())
print("Saldo de Carlos:", nomina.consultar_saldo())
