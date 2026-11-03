class ServicioEmail:
    def enviar_correo(self, mensaje: str, destino: str):
        print(f"Enviando Email a {destino}: {mensaje}")


class NotificadorUsuario:
    def _init_(self):
        # Dependencia rígida de bajo nivel
        self.emisor = ServicioEmail()

    def notificar(self, mensaje: str, destino: str):
        self.emisor.enviar_correo(mensaje, destino)