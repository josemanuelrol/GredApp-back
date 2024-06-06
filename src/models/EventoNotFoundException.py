# Excepción personalizada que indica que no se ha encontrado ningún evento
class EventoNotFoundException(Exception):
    def __init__(self):
        super().__init__("Evento no encontrado")