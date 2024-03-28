import uuid
from datetime import datetime

class Tarea:
    
    def __init__(self, tiempo, recurso, ubicacion):
        self.uuid = uuid.uuid4()
        self.tiempo = tiempo
        self.recurso = recurso
        self.ubicacion = ubicacion
        self.fecha_solicitud = datetime.now()
        self.fecha_cierre = None

    def obtener_tiempo_estimado(self):
        pass

    def obtener_recursos_necesarios(self):
        pass

    def actualizar_tiempo_estimado(self):
        pass

    def asignar_a_brigada(self):
        pass

    def completar_tarea(self):
        self.fecha_cierre = datetime.now()

    def calcular_prioridad(self):
        pass