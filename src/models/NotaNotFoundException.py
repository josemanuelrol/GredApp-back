# Excepción personalizada que indica que no se ha encontrado ninguna nota 
class NotaNotFoundException(Exception):
    def __init__(self):
        super().__init__("Nota no encontrada")