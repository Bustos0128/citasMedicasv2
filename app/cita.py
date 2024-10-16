class Cita:
    def __init__(self, paciente, medico, fecha_hora, motivo):
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora
        self.motivo = motivo
        self.motivo_cancelacion = None
        self.estado = "Programada" 

    def recordatorio_cita(self):
        if self.estado == "Programada":
            print(f"Enviando recordatorio de cita al paciente {self.paciente.nombre} para el {self.fecha_hora}")
        else:
            print(f"La cita no está programada, estado actual: {self.estado}")

    def reprogramar_cita(self, nueva_fecha_hora):
        if self.estado == "Cancelada":
            print(f"No se puede reprogramar una cita que ha sido cancelada.")
            return
        
        if self.medico.verificar_disponibilidad(nueva_fecha_hora):
            print(f"Cita reprogramada del {self.fecha_hora} al {nueva_fecha_hora}")
            self.fecha_hora = nueva_fecha_hora
        else:
            print(f"No hay disponibilidad para reprogramar la cita en la fecha {nueva_fecha_hora}")

    def cancelar_cita(self, motivo):
        if self.estado != "Programada":
            print(f"La cita ya está {self.estado}, no se puede cancelar nuevamente.")
            return
        
        self.motivo_cancelacion = motivo
        self.estado = "Cancelada"
        print(f"La cita ha sido cancelada por {self.paciente.nombre}, debido a: {self.motivo_cancelacion}")

    def __repr__(self):
        return f"Cita del paciente {self.paciente.nombre} con el Dr. {self.medico.nombre}, programada para el {self.fecha_hora}."
