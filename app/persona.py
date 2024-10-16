class Persona:
    def __init__(self, identificacion, nombre, celular, correo, whatsapp=None):
        self.identificacion = identificacion
        self.nombre = nombre
        self.celular = celular
        self.correo = correo
        self.whatsapp = whatsapp if whatsapp else "No registrado"  # Valor por defecto

    def __str__(self):
        return f'{self.nombre} (Correo: {self.correo}, Celular: {self.celular}, WhatsApp: {self.whatsapp})'
    
    def actualizar_celular(self, nuevo_celular):
        self.celular = nuevo_celular
        print(f"Celular de {self.nombre} actualizado a {self.celular}.")
    
    def actualizar_correo(self, nuevo_correo):
        self.correo = nuevo_correo
        print(f"Correo de {self.nombre} actualizado a {self.correo}.")

    def actualizar_whatsapp(self, nuevo_whatsapp):
        self.whatsapp = nuevo_whatsapp
        print(f"WhatsApp de {self.nombre} actualizado a {self.whatsapp}.")
