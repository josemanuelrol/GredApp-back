# Excepción personalizada que indica que no se ha encontrado ninguna tarea
class TareaNotFoundException(Exception):
    def __init__(self):
        super().__init__("Tarea no encontrada")