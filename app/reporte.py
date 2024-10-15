class Reporte:
    def __init__(self, tipo_reporte, fecha_inicio, fecha_fin):
        self.tipo_reporte = tipo_reporte
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def generar_reporte(self):
        pass

    def exportar_Excel(self):
        print(f"Exportando reporte {self.tipo_reporte} a Excel")


class ReporteDemanda(Reporte):
    def __init__(self, tipo_reporte, fecha_inicio, fecha_fin, medico):
        super().__init__(tipo_reporte, fecha_inicio, fecha_fin)
        self.medico = medico

    def generar_reporte(self):
        print(f"Generando reporte de demanda para el Dr. {self.medico.nombre}")


class ReporteTendencias(Reporte):
    def __init__(self, tipo_reporte, fecha_inicio, fecha_fin, citas_agendadas):
        super().__init__(tipo_reporte, fecha_inicio, fecha_fin)
        self.citas_agendadas = citas_agendadas

    def generar_reporte(self):
        print("Generando reporte de tendencias...")


class ReporteCancelaciones(Reporte):
    def __init__(self, tipo_reporte, fecha_inicio, fecha_fin, motivo_cancelacion):
        super().__init__(tipo_reporte, fecha_inicio, fecha_fin)
        self.motivo_cancelacion = motivo_cancelacion

    def generar_reporte(self):
        print(
            f"Generando reporte de cancelaciones por motivo: {self.motivo_cancelacion}")


class ReporteAusentismo(Reporte):
    def __init__(self, tipo_reporte, fecha_inicio, fecha_fin, citas_ausentes):
        super().__init__(tipo_reporte, fecha_inicio, fecha_fin)
        self.citas_ausentes = citas_ausentes

    def generar_reporte(self):
        print("Generando reporte de ausentismo...")
