#Imports
from flask import current_app
import jwt
import datetime
import bcrypt
from bson import json_util
from src.services.UserService import UserService

# Servicio encargado del apartado de autorización de la API, tiene los métodos necesarios para hacer login, verificar la contraseña, cambiar la contraseñá y generar el token JWT.
class AuthService():

    # Constructor
    def __init__(self,userService:UserService):
        self.userService = userService

    # Método que realiza el lógin en la aplicación
    def login(self,usuario,password):
        current_app.logger.info("Service -> login()")
        #Obtener usuario de la BD
        try:
            user = json_util.loads(self.userService.obtener_usuario_por_username(usuario))
        except Exception:
            raise Exception("Usuario o Contraseña Incorrecta")
        #Verificamos la contraseña
        self.verifyPassword(password, user)
        
        token = self.generateToken(str(user['_id']))
        return token,user
    
    # Método que verifica si la contraseña recibida coincide con la del usuario que se pasa por parámetro.
    def verifyPassword(self, input_password, user):
        stored_password = user['password']
        if not stored_password:
            raise ValueError("Contraseña vacía")
        if not bcrypt.checkpw(input_password.encode('utf-8'), stored_password.encode('utf-8')):
            raise ValueError("Usuario o Contraseña Incorrecta")
        
    # Método que se encarga de hacer las comprobaciones necesarias antes de cambiar la contraseña
    def changePassword(self,user_id, body):
        current_app.logger.info("Service -> changePassword()")
        password = body['password']
        newPassword = body['newPassword']
        confirmPassword = body['confirmPassword']
        user = json_util.loads(self.userService.obtener_usuario_por_id(user_id))
        if not password or not newPassword or not confirmPassword:
            raise ValueError("Algunas de las contraseñas están vacías")
        if not bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            raise ValueError('La contraseña actual no es correcta')
        if newPassword != confirmPassword:
            raise ValueError("Las contraseñas no coinciden")
        response = self.userService.cambiar_contraseña(user_id,newPassword)
        return response

    # Método que genera un token con una expiración de 7 días.  
    def generateToken(self,user_id):
        payload = {
            'id':user_id,
            'iat': datetime.datetime.now().astimezone(),
            'exp': datetime.datetime.now().astimezone() + datetime.timedelta(days=7)
        }
        key = current_app.config['SECRET_KEY']
        token = jwt.encode(payload, key, algorithm='HS256')
        return token
        