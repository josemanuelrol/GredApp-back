class CalendarioNotFoundException(Exception):
    def __init__(self):
        super().__init__("Calendario no encontrado")