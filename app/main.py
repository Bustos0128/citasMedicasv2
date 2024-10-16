import json
import unidecode
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich.text import Text
from app.hospital import Hospital
from app.persona_factory import PersonasFactory

console = Console()

# Función para cargar especialidades desde archivo de médicos
def cargar_especialidades(archivo_medicos):
    try:
        with open(archivo_medicos, 'r') as file:
            medicos = json.load(file)
            especialidades = {medico['especialidad'] for medico in medicos}
            return especialidades
    except FileNotFoundError:
        console.print(f"[bold red]El archivo {archivo_medicos} no se encontró.[/bold red]")
        return set()

especialidades_disponibles = cargar_especialidades('data/medicos.json')

# Función para normalizar texto eliminando acentos y usando minúsculas
def normalizar_texto(texto):
    return unidecode.unidecode(texto).lower()

# Función para mostrar el menú principal
def mostrar_menu():
    console.print(Panel.fit("[bold cyan]--- Menú ---[/bold cyan]\n\n"
                            "1. Agregar persona\n"
                            "2. Pedir cita\n"
                            "3. Cancelar cita\n"
                            "4. Asignar médico de preferencia\n"
                            "5. Ver citas pendientes\n"
                            "6. Salir", title="Sistema de Citas Médicas", title_align="left"))

# Función para agregar una persona (médico o paciente)
def agregar_persona(hospital):
    while True:
        tipo_persona = Prompt.ask(
            "[bold cyan]Ingrese el tipo de persona (médico o paciente)[/bold cyan]",
            show_choices=False  
        ).lower()

        if tipo_persona not in ["medico", "paciente"]:
            console.print("[bold red]Opción inválida. Por favor, seleccione entre las opciones: médico o paciente.[/bold red]")
            continue

        identificacion = IntPrompt.ask("[bold cyan]Ingrese la identificación (solo números)[/bold cyan]")
        nombre = Prompt.ask("[bold cyan]Ingrese el nombre[/bold cyan]")
        celular = IntPrompt.ask("[bold cyan]Ingrese el número de celular[/bold cyan]")

        if tipo_persona == "medico":
            while True:
                especialidad = Prompt.ask(f"[bold cyan]Ingrese la especialidad (disponibles: {', '.join(especialidades_disponibles)})[/bold cyan]").lower()
                
                # Normalizamos la especialidad ingresada y las especialidades disponibles
                especialidad_normalizada = normalizar_texto(especialidad)
                especialidades_disponibles_normalizadas = {normalizar_texto(esp) for esp in especialidades_disponibles}

                if especialidad_normalizada in especialidades_disponibles_normalizadas:
                    # Encontramos la especialidad con su capitalización correcta
                    especialidad_correcta = next(esp for esp in especialidades_disponibles if normalizar_texto(esp) == especialidad_normalizada)
                    break
                else:
                    console.print(f"[bold red]Especialidad inválida. Por favor, elija una de las disponibles.[/bold red]")

            persona = PersonasFactory.crear_persona("medico", identificacion, nombre, celular, especialidad_correcta)
            hospital.agregar_medico(persona)
            console.print(f"[bold green]Médico {nombre} agregado con éxito.[/bold green]")

        elif tipo_persona == "paciente":
            correo = Prompt.ask("[bold cyan]Ingrese el correo electrónico[/bold cyan]", default="sin_correo@ejemplo.com")
            whatsapp = Prompt.ask("[bold cyan]Ingrese el número de WhatsApp (opcional)[/bold cyan]", default=None)
            persona = PersonasFactory.crear_persona("paciente", identificacion, nombre, celular, correo=correo)
            persona.actualizar_whatsapp(whatsapp)
            hospital.agregar_paciente(persona)
            console.print(f"[bold green]Paciente {nombre} agregado con éxito.[/bold green]")
        break

# Función para pedir una cita
def pedir_cita(hospital):
    id_paciente = Prompt.ask("[bold cyan]Ingrese la identificación del paciente[/bold cyan]")
    id_medico = Prompt.ask("[bold cyan]Ingrese la identificación del médico[/bold cyan]")
    fecha = Prompt.ask("[bold cyan]Ingrese la fecha de la cita (YYYY-MM-DD)[/bold cyan]")
    motivo = Prompt.ask("[bold cyan]Ingrese el motivo de la cita[/bold cyan]")

    paciente = hospital.buscar_paciente(id_paciente)
    medico = hospital.buscar_medico(id_medico)

    if paciente and medico:
        hospital.agendar_cita(paciente, medico, fecha, motivo)
        console.print("[bold green]Cita agendada con éxito.[/bold green]")
    else:
        console.print("[bold red]Paciente o médico no encontrado.[/bold red]")

# Función para cancelar una cita
def cancelar_cita(hospital):
    id_paciente = Prompt.ask("[bold cyan]Ingrese la identificación del paciente[/bold cyan]")
    paciente = hospital.buscar_paciente(id_paciente)

    if paciente:
        citas_pendientes = [cita for cita in hospital.agenda_general.citas_pendientes if cita.paciente == paciente]
        if citas_pendientes:
            table = Table(title="Citas Pendientes")
            table.add_column("Índice", justify="center")
            table.add_column("Fecha", justify="center")
            table.add_column("Médico", justify="center")
            for i, cita in enumerate(citas_pendientes, 1):
                table.add_row(str(i), cita.fecha_hora, cita.medico.nombre)
            console.print(table)

            opcion_cita = IntPrompt.ask("[bold cyan]Seleccione la cita a cancelar[/bold cyan]", choices=[str(i+1) for i in range(len(citas_pendientes))])
            cita_a_cancelar = citas_pendientes[int(opcion_cita) - 1]
            hospital.cancelar_cita(cita_a_cancelar)
            console.print(f"[bold green]Cita con {cita_a_cancelar.medico.nombre} cancelada.[/bold green]")
        else:
            console.print(f"[bold red]No hay citas pendientes para el paciente {paciente.nombre}.[/bold red]")
    else:
        console.print("[bold red]Paciente no encontrado.[/bold red]")

# Función para asignar un médico de preferencia a un paciente
def asignar_medico_preferencia(hospital):
    id_paciente = Prompt.ask("[bold cyan]Ingrese la identificación del paciente[/bold cyan]")
    id_medico = Prompt.ask("[bold cyan]Ingrese la identificación del médico[/bold cyan]")

    paciente = hospital.buscar_paciente(id_paciente)
    medico = hospital.buscar_medico(id_medico)

    if paciente and medico:
        paciente.asignar_medico_preferencia(medico)
        console.print(f"[bold green]Médico {medico.nombre} asignado como preferido para {paciente.nombre}.[/bold green]")
    else:
        console.print("[bold red]Paciente o médico no encontrado.[/bold red]")

def ver_citas_pendientes(hospital):
    id_paciente = input("Ingrese la identificación del paciente: ")
    paciente = hospital.buscar_paciente(id_paciente)
    
    if paciente:
        # Consultar las citas del paciente en la agenda centralizada del hospital
        citas_paciente = [cita for cita in hospital.agenda_general.citas_pendientes if cita.paciente == paciente]
        if citas_paciente:
            print(f"Citas pendientes para el paciente {paciente.nombre}:")
            for cita in citas_paciente:
                print(f"- Fecha y hora: {cita.fecha_hora}, Médico: {cita.medico.nombre}, Motivo: {cita.motivo}")
        else:
            print(f"No hay citas pendientes para el paciente {paciente.nombre}.")
    else:
        print(f"No se encontró ningún paciente con la identificación {id_paciente}.")


# Función principal que inicia el programa
def main():
    hospital = Hospital.get_instance()
    hospital.cargar_pacientes('data/pacientes.csv')
    hospital.cargar_medicos('data/medicos.json')
    hospital.cargar_citas('data/citas.csv')

    while True:
        mostrar_menu()
        opcion = Prompt.ask("[bold cyan]Seleccione una opción[/bold cyan]", choices=["1", "2", "3", "4", "5", "6"])

        if opcion == "1":
            agregar_persona(hospital)
        elif opcion == "2":
            pedir_cita(hospital)
        elif opcion == "3":
            cancelar_cita(hospital)
        elif opcion == "4":
            asignar_medico_preferencia(hospital)
        elif opcion == "5":
            ver_citas_pendientes(hospital)
        elif opcion == "6":
            console.print("[bold yellow]Saliendo del sistema...[/bold yellow]")
            break
        else:
            console.print("[bold red]Opción inválida. Intente de nuevo.[/bold red]")

if __name__ == "__main__":
    main()
