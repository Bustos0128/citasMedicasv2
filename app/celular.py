
from notificacion import Notificacion

class Celular(Notificacion):
    def enviar_notificacion(self, mensaje: str):
        if self.persona.celular:
            print(f'Enviando mensaje a {self.persona.celular}: {mensaje}')
        else:
            print('Número de celular no disponible para esta persona.')