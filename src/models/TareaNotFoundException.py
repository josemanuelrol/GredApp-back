class TareaNotFoundException(Exception):
    def __init__(self):
        super().__init__("Tarea no encontrada")