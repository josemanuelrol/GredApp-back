class EventoNotFoundException(Exception):
    def __init__(self):
        super().__init__("Evento no encontrado")