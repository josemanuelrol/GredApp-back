# Excepción personalizada que indica que no se ha encontrado ninguna lista de tareas
class ListaTareasNotFoundException(Exception):
    def __init__(self):
        super().__init__("Lista de tareas no encontrada")