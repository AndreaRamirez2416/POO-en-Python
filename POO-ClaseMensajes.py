class Mensaje:
    def __init__(self, remitente, destinatario, contenido):
        self.remitente = remitente
        self.destinatario = destinatario
        self.contenido = contenido
    def mostrar_mensaje(self):
        print(f"De: {self.remitente}")
        print(f"Para: {self.destinatario}")
        print(f"Mensaje: {self.contenido}")

Mensajes=[]
print("SISTEMA DE GESTIÓN DE MENSAJES")
Opcion=""

while Opcion!="3":
    print("1. Crear mensaje")
    print("2. Mostrar mensajes")
    print("3. Salir")
    Opcion=input("Seleccione una opción: ")

    if Opcion=="1":
        remitente=input("Ingrese el remitente: ")
        destinatario=input("Ingrese el destinatario: ")
        contenido=input("Ingrese el contenido del mensaje: ")
        mensaje=Mensaje(remitente, destinatario, contenido)
        Mensajes.append(mensaje)
        print("Mensaje creado exitosamente.")
    elif Opcion=="2":
        if len(Mensajes)==0:
            print("No hay mensajes para mostrar.")
        else:
            for i, mensaje in enumerate(Mensajes):
                print(f"\nMensaje {i+1}:")
                mensaje.mostrar_mensaje()
    elif Opcion=="3":
        print("Saliendo del sistema de gestión de mensajes.")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")



    

