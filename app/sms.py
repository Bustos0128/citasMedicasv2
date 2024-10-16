from notificacion import Notificacion

class SMS(Notificacion):
    def enviar_notificacion(self, mensaje: str):
        if self.persona.celular:
            print(f'Enviando SMS al celular {self.persona.celular}: {mensaje}')
        else:
            print('Número de celular no disponible para enviar SMS.')
