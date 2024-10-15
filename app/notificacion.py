from aplicacion import Aplicacion
from celular import Celular
from correo import Correo


class Notificacion:
    def __init__(self):
        self.correo = Correo()
        self.celular = Celular()
        self.aplicacion = Aplicacion()

    def enviar_notificacion(self):
        return self.aplicacion.enviar_notificacion()

    def verificar_correo(self):
        print(f"Verificando correo {self.correo}")
