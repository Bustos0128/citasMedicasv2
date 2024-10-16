import csv
import json
from datetime import datetime
from app.agenda import Agenda
from app.cita import Cita
from app.paciente import Paciente
from app.medico import Medico

class Hospital:
    __instance = None

    def __init__(self):
        if Hospital.__instance is None:
            Hospital.__instance = self
            self.pacientes = []
            self.medicos = []
            self.agenda_general = Agenda()  # Agenda centralizada en el hospital
        else:
            print("Instancia de Hospital ya existe.")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls()
        return cls.__instance

    def agregar_paciente(self, paciente):
        if paciente not in self.pacientes:
            self.pacientes.append(paciente)
            print(f"Paciente {paciente.nombre} agregado.")
        else:
            print(f"El paciente {paciente.nombre} ya está registrado.")

    def agregar_medico(self, medico):
        if medico not in self.medicos:
            self.medicos.append(medico)
            print(f"Médico {medico.nombre} agregado.")
        else:
            print(f"El médico {medico.nombre} ya está registrado.")
            
    def buscar_paciente(self, identificacion):
        for paciente in self.pacientes:
            if paciente.identificacion == identificacion:
                return paciente
        return None

    def agendar_cita(self, paciente, medico, fecha, motivo):
        if self.verificar_disponibilidad(medico, fecha):
            nueva_cita = Cita(paciente, medico, fecha, motivo)
            self.agenda_general.agregar_cita(nueva_cita)  # Agregamos a la agenda general del hospital
            print(f"Cita agendada con éxito para {paciente.nombre} con el Dr. {medico.nombre} el {fecha}.")
        else:
            print(f"No hay disponibilidad con el Dr. {medico.nombre} en la fecha {fecha}.")

    def cancelar_cita(self, cita):
        """Cancela una cita y la mueve, si es necesario."""
        self.agenda_general.cancelar_y_mover_cita(cita)
        print(f"Cita cancelada para el paciente {cita.paciente.nombre} con el Dr. {cita.medico.nombre}.")

    def verificar_disponibilidad(self, medico, fecha):
        """Verifica si un médico está disponible en una fecha específica en la agenda centralizada del hospital."""
        for cita in self.agenda_general.citas_pendientes:
            if cita.medico == medico and cita.fecha_hora == fecha:
                return False  # Ya tiene una cita programada para esa fecha y hora
        return True

    def ver_citas_pendientes(self):
        id_paciente = input("Ingrese la identificación del paciente: ")
        paciente = self.buscar_paciente(id_paciente)
        
        if paciente:
            citas_paciente = [cita for cita in self.agenda_general.citas_pendientes if cita.paciente == paciente]
            if citas_paciente:
                print(f"Citas pendientes para el paciente {paciente.nombre}:")
                for cita in citas_paciente:
                    print(f"- Fecha y hora: {cita.fecha_hora}, Médico: {cita.medico.nombre}, Motivo: {cita.motivo}")
            else:
                print(f"No hay citas pendientes para el paciente {paciente.nombre}.")
        else:
            print(f"No se encontró ningún paciente con la identificación {id_paciente}.")

    def cargar_pacientes(self, archivo):
        try:
            with open(archivo, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if 'identificación' in row and 'nombre_completo' in row and 'celular' in row and 'correo' in row:
                        paciente = Paciente(
                            identificacion=row['identificación'],  
                            nombre=row['nombre_completo'],
                            celular=row['celular'],
                            correo=row['correo']
                        )
                        self.agregar_paciente(paciente)
                    else:
                        print(f"Faltan datos requeridos en una fila del archivo {archivo}: {row}")
        except FileNotFoundError:
            print(f"El archivo {archivo} no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar pacientes: {e}")

    def cargar_medicos(self, archivo):
        try:
            with open(archivo, mode='r', encoding='utf-8') as f:
                medicos_data = json.load(f)
                for medico_data in medicos_data:
                    correo = medico_data.get('correo', 'sin_correo@sin.com')
                    medico = Medico(
                        identificacion=medico_data['id'],
                        nombre=medico_data['nombre'],
                        celular=medico_data['celular'],
                        especialidad=medico_data['especialidad'],
                        correo=correo
                    )
                    self.agregar_medico(medico)
        except FileNotFoundError:
            print(f"El archivo {archivo} no fue encontrado.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON {archivo}.")
        except Exception as e:
            print(f"Error al cargar médicos: {e}")

    def cargar_citas(self, archivo):
        try:
            with open(archivo, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if 'paciente' in row and 'medicos' in row and 'fecha_hora' in row:
                        paciente_id = row['paciente']
                        medico_id = row['medicos']
                        try:
                            fecha_hora = datetime.strptime(row['fecha_hora'], '%Y-%m-%d %H:%M:%S')
                        except ValueError:
                            print(f"Error en el formato de fecha y hora: {row['fecha_hora']}")
                            continue  

                        paciente = next((p for p in self.pacientes if p.identificacion == paciente_id), None)
                        medico = next((m for m in self.medicos if m.identificacion == medico_id), None)

                        if paciente and medico:
                            cita = Cita(paciente, medico, fecha_hora)
                            self.agenda_general.agregar_cita(cita) 
                        else:
                            print(f"No se pudo cargar la cita. Paciente o médico no encontrado: {paciente_id}, {medico_id}")
                    else:
                        print(f"Faltan datos requeridos en una fila del archivo {archivo}: {row}")
        except FileNotFoundError:
            print(f"El archivo {archivo} no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar citas: {e}")
