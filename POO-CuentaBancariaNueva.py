from abc import ABC, abstractmethod


class CuentaBancaria(ABC):
    """Clase abstracta que define el contrato para el resto de cuentas"""

    def __init__(self, numero_cuenta:str, titular:str, saldo:float=0):
        self._numero_cuenta = numero_cuenta
        self._titular = titular
        self._saldo = saldo
        self._historial:list [dict] = []

    def depositar(self, monto:float)->bool:
        """Metodo que es heredado por las clases hijas, permite depositar dinero en la cuenta"""
        if monto > 0:
            self._saldo += monto
            self._registrar_transaccion("deposito", monto)
            return True
        return False

    def retirar(self, monto:float)->bool:
        """Este metodo puede ser sobreescrito por las clases hijas, permite retirar dinero de la cuenta"""
        comision = self._calcular_comision(monto)
        total_retiro = monto + comision
        if total_retiro <= self._saldo and monto > 0:
            self._saldo -= total_retiro
            self._registrar_transaccion("retiro", monto, f"comision: ${comision}")
            return True
        return False

    def _registrar_transaccion(self, tipo:str, monto:float, detalle:str=""):
        """metodo privado que registra las transacciones realizadas en la cuenta"""
        transaccion = {
            "tipo": tipo,
            "monto": monto,
            "detalle": detalle
        }
        self._historial.append(transaccion)

    @abstractmethod
    def calcular_comision(self, monto:float)->float:
        """Metodo abstracto, cada tipo de cuenta debe implementar su propia logica para calcular la comision"""
        pass

    @abstractmethod    
    def get_tipo_cuenta(self)->str:
        """Metodo que retorna el tipo de cuenta"""
        pass

    """Getters y Setters"""
    @property    
    def saldo(self)->float:
        """Metodo que retorna el saldo actual de la cuenta"""
        return self._saldo

    @property
    def numero_cuenta(self)->str:
        """Metodo que retorna el numero de cuenta"""
        return self._numero_cuenta

    def get_historial(self)->list:
        """Metodo que retorna el historial de transacciones de la cuenta"""
        return self._historial.copy()



    def sumar(self, a,b):
        """Metodo que suma dos numeros"""
        return a + b

    def sumar(self, a,b,c=0):
        """Metodo que suma tres numeros"""
        return a + b + c

cta=CuentaBancaria("12345", "Juan Perez", 1000)
cta.sumar(1,2,5)


    
    
   





    

    

    

        