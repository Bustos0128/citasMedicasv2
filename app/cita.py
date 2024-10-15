class Cita:
    def __init__(self, paciente, medico, fecha):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.motivo_cancelacion = None

    def recordatorio_cita(self):
        print(f"Enviando notificación al paciente {self.paciente.nombre}")

    def reprogramar_cita(self, nueva_fecha):
        if self.medico.verificar_disponibilidad(nueva_fecha):
            print(f"Cita reprogramada del {self.fecha} al {nueva_fecha}")
            self.fecha = nueva_fecha
        else:
            print(
                f"No hay disponibilidad para reprogramar la cita en la fecha {nueva_fecha}")

    def cancelar_cita(self, motivo):
        self.motivo_cancelacion = motivo
        print(
            f"La cita ha sido cancelada por {self.paciente.nombre}, debido a: {self.motivo_cancelacion}")

    def __repr__(self):
        # return f"Cita programada para el {self.fecha}" -> return f"Cita del paciente {self.paciente.nombre} con el Dr. {self.medico.nombre} programada para el {self.fecha}"
        return f"Cita del paciente {self.paciente.nombre} con el Dr. {self.medico.nombre} programada para el {self.fecha}"
