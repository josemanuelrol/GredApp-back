#Imports
from flask import request, current_app
import jwt
import datetime
import locale
import bcrypt
from bson import json_util
from src.services.UserService import UserService

#Configuramos la localicazión al español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

class AuthService():

    def __init__(self,userService:UserService):
        self.userService = userService

    def login(self,usuario,password):
        #Obtener usuario de la BD
        user = json_util.loads(self.userService.obtener_usuario_por_username(usuario))
        
        #Verificamos la contraseña
        if not self.verifyPassword(password, user):
            raise Exception("Contraseña Incorrecta")
        
        token = self.generateToken(str(user['_id']))
        return token
    
    def verifyPassword(self, input_password, user):
        try:
            stored_password = user['password']
            if not stored_password:
                raise ValueError("No existe esa contraseña")
            if not bcrypt.checkpw(input_password.encode('utf-8'), stored_password.encode('utf-8')):
                raise ValueError("Contraseña Incorrecta.")
            return True
        except ValueError:
            return False
        
    def generateToken(self,user_id):
        payload = {
            'id':user_id,
            'iat': datetime.datetime.now().astimezone(),
            'exp': datetime.datetime.now().astimezone() + datetime.timedelta(hours=24)
        }
        key = current_app.config['SECRET_KEY']
        token = jwt.encode(payload, key, algorithm='HS256')
        return token
        