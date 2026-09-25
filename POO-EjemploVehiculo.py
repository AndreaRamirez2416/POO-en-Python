class Vehiculo:

    def __init__(self, tipo, color, marca):
        self.tipo = tipo
        self.color = color
        self.marca = marca

    def Encender(self):
        print ("El vehiculo esta encendido ")

    def Pitar(self):
        print ("El vehiculo esta pitando ")

    def Apagar(self):
        print ("El vehiculo esta apagado ")

Moto1 = Vehiculo("Moto", "Negro", "Yamaha")
Moto2 = Vehiculo("Moto", "Azul", "Honda")
Carro1 = Vehiculo("Carro", "Rojo", "Toyota")
Carro2 = Vehiculo("Carro", "Blanco", "Nissan")

print (Moto1.Encender())
print (Moto1.Pitar())
print (Moto1.Apagar())
print (Moto2.Encender())
print (Moto2.Pitar())
print (Moto2.Apagar())
print (Carro1.Encender())
print (Carro1.Pitar())
print (Carro1.Apagar())
print (Carro2.Encender())
print (Carro2.Pitar())
print (Carro2.Apagar())