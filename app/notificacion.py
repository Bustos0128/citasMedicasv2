from aplicacion import Aplicacion
from abc import ABC, abstractmethod
from persona import Persona

class Notificacion(ABC):
    def __init__(self, persona: Persona):
        self.persona = persona

    @abstractmethod
    def enviar_notificacion(self, mensaje: str):
        pass
