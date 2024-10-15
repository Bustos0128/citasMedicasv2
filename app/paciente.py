from persona import Persona
from agenda import Agenda
from cita import Cita


class Paciente(Persona):
    def __init__(self, identificacion, nombre, celular, correo):
        super().__init__(identificacion, nombre, celular)
        self.correo = correo
        self.medico_preferencia = None
        self.agenda = Agenda()  # Agenda del paciente

    def pedir_cita(self, medico, fecha, motivo):
        # Verificar si el médico tiene disponibilidad
        if medico.verificar_disponibilidad(fecha):
            # Cita(medico, fecha, motivo) -> Cita(self, medico, fecha)
            nueva_cita = Cita(self, medico, fecha)
            medico.agenda.agregar_cita(nueva_cita)
            self.agenda.agregar_cita(nueva_cita)
            # print(f"Cita solicitada para el paciente {self.nombre} con el Dr. {medico.nombre}")
        else:
            print(
                f"No hay disponibilidad con el Dr. {medico.nombre} en la fecha {fecha}")

    def cancelar_cita(self, cita):
        # Cancelar la cita y notificar tanto al médico como al paciente
        cita.cancelar_cita()
        print(f"Cita cancelada por el paciente {self.nombre}")

    def asignar_medico_preferencia(self, medico):
        self.medico_preferencia = medico
        print(
            f"El médico {medico.nombre} ha sido asignado como preferencia para el paciente {self.nombre}")
