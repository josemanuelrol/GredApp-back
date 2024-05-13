class UserNotFoundException(Exception):
    def __init__(self):
        super().__init__("Usuario no encontrado")