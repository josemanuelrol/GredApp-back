# Excepción personalizada que indica que no se ha encontrado ningún usuario
class UserNotFoundException(Exception):
    def __init__(self):
        super().__init__("Usuario no encontrado")