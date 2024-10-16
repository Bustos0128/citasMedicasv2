class Agenda:
    def __init__(self):
        self.historico_citas = []  # Todas las citas realizadas o canceladas.
        self.citas_pendientes = []  # Citas que están pendientes de realizarse.
    
    def agregar_cita(self, cita):
        if cita not in self.citas_pendientes:
            self.citas_pendientes.append(cita)
            print(f"Cita añadida: {cita}")
        else:
            print(f"La cita ya está en la lista de citas pendientes.")

    def cancelar_y_mover_cita(self, cita, nueva_fecha_hora):
        if cita in self.citas_pendientes:
            cita.cancelar_cita("Reprogramación")
            self.citas_pendientes.remove(cita)
            cita.reprogramar_cita(nueva_fecha_hora)
            self.agregar_cita(cita)  # Reagendamos la cita.
            print(f"La cita ha sido movida a {nueva_fecha_hora}")
        else:
            print(f"La cita no está pendiente, no se puede reprogramar.")

    def finalizar_cita(self, cita):
        if cita in self.citas_pendientes:
            self.citas_pendientes.remove(cita)
            self.historico_citas.append(cita)
            print(f"Cita con el Dr. {cita.medico.nombre} el {cita.fecha_hora} ha sido completada")
        else:
            print(f"La cita no está en la lista de pendientes.")

    def listar_citas_pendientes(self):
        if self.citas_pendientes:
            print("Citas pendientes:")
            for cita in self.citas_pendientes:
                print(cita)
        else:
            print("No hay citas pendientes en la agenda.")

    def listar_historico_citas(self):
        if self.historico_citas:
            print("Histórico de citas:")
            for cita in self.historico_citas:
                print(cita)
        else:
            print("No hay citas en el historial.")
