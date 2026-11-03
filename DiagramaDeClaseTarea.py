from abc import ABC, abstractmethod


# 1. La Abstracción (Interfaz)
class CanalNotificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str, destino: str):
        pass


# 2. Clases de bajo nivel (Implementaciones concretas)
class ServicioEmail(CanalNotificacion):
    def enviar(self, mensaje: str, destino: str):
        print(f"📧 [Email] Enviado a {destino}: {mensaje}")


class ServicioSMS(CanalNotificacion):
    def enviar(self, mensaje: str, destino: str):
        print(f"💬 [SMS] Enviado a {destino}: {mensaje}")


class ServicioWhatsApp(CanalNotificacion):
    def enviar(self, mensaje: str, destino: str):
        print(f"🟢 [WhatsApp] Enviado a {destino}: {mensaje}")


# 3. Clase de alto nivel (Totalmente desacoplada)
class NotificadorUsuario:
    def __init__(self, canal: CanalNotificacion):
        # Recibe cualquier canal que cumpla con la interfaz
        self.canal = canal

    def enviar_alerta(self, mensaje: str, destino: str):
        self.canal.enviar(mensaje, destino)


# === Uso del sistema ===

# Enviar una alerta por Email
notificador_email = NotificadorUsuario(ServicioEmail())
notificador_email.enviar_alerta("Tu paquete ha salido", "juan@email.com")

# Enviar una alerta por SMS cambiando solo el canal inyectado
notificador_sms = NotificadorUsuario(ServicioSMS())
notificador_sms.enviar_alerta("Código de verificación: 4821", "+573001234567")

notificador_whatsapp = NotificadorUsuario(ServicioWhatsApp())
notificador_whatsapp.enviar_alerta("¡Tu pedido ha sido entregado!", "+573001234567")