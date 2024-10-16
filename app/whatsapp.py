from notificacion import Notificacion

class WhatsApp(Notificacion):
    def enviar_notificacion(self, mensaje: str):
        if self.persona.whatsapp:
            print(f'Enviando WhatsApp a {self.persona.whatsapp}: {mensaje}')
        else:
            print('Número de WhatsApp no disponible para esta persona.')
