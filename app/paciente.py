from app.cita import Cita
from app.persona import Persona

class Paciente(Persona):
    def __init__(self, identificacion, nombre, celular, correo):
        super().__init__(identificacion, nombre, celular, correo)
        self.medico_preferencia = None  

    def asignar_medico_preferencia(self, medico):
        self.medico_preferencia = medico
        print(f"El médico {medico.nombre} ha sido asignado como preferencia para el paciente {self.nombre}.")

    def pedir_cita(self, medico, fecha, motivo):
        if medico:
            # Importar Hospital dentro del método para evitar circularidad
            from app.hospital import Hospital
            hospital = Hospital.get_instance()  # Obtener instancia del hospital
            hospital.agendar_cita(self, medico, fecha, motivo)
        else:
            print("Error: No se especificó un médico.")

    def cancelar_cita(self, cita):
        # Importar Hospital dentro del método para evitar circularidad
        from app.hospital import Hospital
        hospital = Hospital.get_instance()  # Acceder a la instancia del Hospital
        hospital.cancelar_cita(cita)  # Cancelar cita en la agenda general
        print(f"Cita cancelada para el paciente {self.nombre} con el Dr. {cita.medico.nombre}.")

    def consultar_citas(self):
        from app.hospital import Hospital
        hospital = Hospital.get_instance()
        citas_paciente = [cita for cita in hospital.agenda_general.citas_pendientes if cita.paciente == self]
        
        if citas_paciente:
            print(f"Citas programadas para {self.nombre}:")
            for cita in citas_paciente:
                print(f"- Cita con {cita.medico.nombre} el {cita.fecha}")
        else:
            print(f"No hay citas programadas para {self.nombre}.")

    def recibir_notificacion(self, mensaje):
        print(f"Notificación para {self.nombre}: {mensaje}")

    def actualizar_informacion(self, celular=None, correo=None):
        if celular:
            self.celular = celular
        if correo:
            self.correo = correo
        print(f"Información actualizada para {self.nombre}: Celular - {self.celular}, Correo - {self.correo}")

    def cargar_datos(self, datos):
        self.identificacion = datos.get('identificacion', self.identificacion)
        self.nombre = datos.get('nombre', self.nombre)
        self.celular = datos.get('celular', self.celular)
        self.correo = datos.get('correo', self.correo)
        print(f"Datos cargados para {self.nombre}: {self.identificacion}, {self.celular}, {self.correo}")
