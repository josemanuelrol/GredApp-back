#Imports
from flask import request, current_app
import jwt

# Clase que contiene un método para verificar la validez del token
class VerifyToken():

    def __init__(self):
        pass

    # Método que verifica la validez del token
    def verifyToken(self):
        try:
            #Obtener el token del encabezado de autorización
            authorization_header = request.headers.get('Authorization')

            if not authorization_header:
                current_app.logger.error("No ha proporcionado el encabezado de autorización")
                return False
            
            #Extraer el token de la cadena de encabezado
            token = authorization_header.split(" ")[1]
            #Obtener la clave secreta
            key = current_app.config['SECRET_KEY']

            #Decodificar el token
            jwt.decode(token, key, algorithms=['HS256'])
            return True
        except Exception as e:
            current_app.logger.error(str(e))
            return False