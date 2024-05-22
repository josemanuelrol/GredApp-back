#Imports
from flask import current_app
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
        try:
            user = json_util.loads(self.userService.obtener_usuario_por_username(usuario))
        except Exception:
            raise Exception("Usuario o Contraseña Incorrecta")
        #Verificamos la contraseña
        self.verifyPassword(password, user)
        
        token = self.generateToken(str(user['_id']))
        return token,user
    
    def verifyPassword(self, input_password, user):
        stored_password = user['password']
        if not stored_password:
            raise ValueError("Usuario o Contraseña Incorrecta")
        if not bcrypt.checkpw(input_password.encode('utf-8'), stored_password.encode('utf-8')):
            raise ValueError("Usuario o Contraseña Incorrecta")
        
    def generateToken(self,user_id):
        payload = {
            'id':user_id,
            'iat': datetime.datetime.now().astimezone(),
            'exp': datetime.datetime.now().astimezone() + datetime.timedelta(hours=24)
        }
        key = current_app.config['SECRET_KEY']
        token = jwt.encode(payload, key, algorithm='HS256')
        return token
        