class NotaNotFoundException(Exception):
    def __init__(self):
        super().__init__("Nota no encontrada")