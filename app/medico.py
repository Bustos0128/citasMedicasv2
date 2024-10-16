from app.persona import Persona

class Medico(Persona):
    def __init__(self, identificacion, nombre, celular, especialidad, correo="sin_correo"):
        super().__init__(identificacion, nombre, celular, correo)
        self.especialidad = especialidad
