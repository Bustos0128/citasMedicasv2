class Agenda:
    def __init__(self):
        self.historico_citas = []
        self.citas_pendientes = []
        self.citas_realizadas = []

    def agregar_cita(self, cita):
        self.citas_pendientes.append(cita)
        print(
            f"Cita agregada para el {cita.fecha} con el Dr. {cita.medico.nombre}")

    def cancelar_y_mover_cita(self, cita):
        self.citas_pendientes.remove(cita)
        print(
            f"La cita del {cita.fecha} ha sido cancelada y movida a otro día.")

    def finalizar_cita(self, cita):
        self.citas_pendientes.remove(cita)
        self.citas_realizadas.append(cita)
        print(
            f"Cita con el Dr. {cita.medico.nombre} el {cita.fecha} ha sido completada")
