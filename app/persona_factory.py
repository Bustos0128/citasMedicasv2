from paciente import Paciente
from medico import Medico


class PersonasFactory:
    @staticmethod
    def crear_persona(tipo, identificacion, nombre, celular, especialidad=None, correo=None):
        if tipo.lower() == 'medico':
            return Medico(identificacion, nombre, celular, especialidad)

        elif tipo.lower() == 'paciente':
            return Paciente(identificacion, nombre, celular, correo)

        else:
            raise ValueError(f"Tipo de persona desconocido: {tipo}")
