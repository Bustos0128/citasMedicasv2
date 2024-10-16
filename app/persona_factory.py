from app.paciente import Paciente
from app.medico import Medico


class PersonasFactory:
    @staticmethod
    def crear_persona(tipo, identificacion, nombre, celular, especialidad=None, correo=None):
        correo = correo if correo else "sin_correo@sin.com"
        
        if tipo.lower() == 'medico':
            if not especialidad:
                raise ValueError("Se requiere una especialidad para crear un médico.")
            return Medico(identificacion, nombre, celular, especialidad, correo)

        elif tipo.lower() == 'paciente':
            return Paciente(identificacion, nombre, celular, correo)

        else:
            raise ValueError(f"Tipo de persona desconocido: {tipo}")
