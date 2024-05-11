#Imports
from flask import current_app
from bson import json_util
from src.database.UserRepository import UserRepository

class UserService():
    
    def __init__(self, userRepository:UserRepository):
        self.userRepository = userRepository

    def crear_usuario(self,body):
        current_app.logger.info("Service -> crear_usuario()")

    def obtener_usuarios(self):
        current_app.logger.info("Services -> obtener_usuarios()")
        response = self.userRepository.get_users()
        return response
    
    def obtener_usuario_por_id(self, id):
        current_app.logger.info("Service -> obtener_usuario_por_id()")
        response = self.userRepository.get_user_by_id(id)
        if response:
            return response
        else:
            raise Exception("Usuario no encontrado")
    
    def modificar_usuario(self,id,body):
        current_app.logger.info("Service -> modificar_usuario()")
        response = self.userRepository.update_user(id,body)
        if response>0:
            return response
        else:
            raise Exception("No se ha podido modificar el usuario")
        
    def eliminar_usuario(self,id):
        current_app.logger.info("Service -> eliminar_usuario()")
        response = self.userRepository.delete_user(id)
        if response>0:
            return response
        else:
            raise Exception("No se ha podido eliminar el usuario")