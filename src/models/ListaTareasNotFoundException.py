class ListaTareasNotFoundException(Exception):
    def __init__(self):
        super().__init__("Lista de tareas no encontrada")