#Imports
from flask import current_app
from bson import json_util
from src.database.UserRepository import UserRepository
from src.database.NotaRepository import NotaRepository
from src.services.ListaTareasService import ListaTareasService
from src.database.ListaTareasRepository import ListaTareasRepository
from src.models.UserNotFoundException import UserNotFoundException

class UserService():
    
    def __init__(self, userRepository:UserRepository, listaTareasService:ListaTareasService, notaRepository:NotaRepository, 
                 listaTareasRepo:ListaTareasRepository):
        self.userRepository = userRepository
        self.listaTareasService = listaTareasService
        self.notaRepository = notaRepository
        self.listaTareasRepo = listaTareasRepo
        

    def crear_usuario(self,body):
        current_app.logger.info("Service -> crear_usuario()")
        try:
            user = json_util.loads(self.obtener_usuario_por_username(body['username']))
        except Exception:
            response = self.userRepository.create_user(body)
            listaTarea = {
                'nombre':'Bandeja de entrada',
                'user_id':response,
                'tareas':[],
            }
            self.listaTareasService.crear_listaTareas(listaTarea)
            if response != 'null':
                return response
            else:
                raise Exception("No se ha podido crear el usuario")
        if user:
            raise Exception("Ya existe un usuario con ese nombre")

    def cambiar_contraseña(self,user_id,new_password):
        current_app.logger.info("Service -> cambiar_contraseña()")
        response = self.userRepository.change_password(user_id, new_password)
        if response > 0:
            return response
        else:
            raise Exception("No se pudo cambiar la contraseñá")

    def obtener_usuarios(self):
        current_app.logger.info("Services -> obtener_usuarios()")
        response = self.userRepository.get_users()
        return response
    
    def obtener_usuario_por_username(self,username):
        current_app.logger.info("Service -> obtener_usuario_por_username()")
        response = self.userRepository.get_user_by_username(username)
        if response != 'null':
            return response
        else:
            raise UserNotFoundException()
    
    def obtener_usuario_por_id(self, id):
        current_app.logger.info("Service -> obtener_usuario_por_id()")
        response = self.userRepository.get_user_by_id(id)
        if response != 'null':
            return response
        else:
            raise UserNotFoundException()
    
    def modificar_usuario(self,id,body):
        current_app.logger.info("Service -> modificar_usuario()")
        self.obtener_usuario_por_id(id)
        response = self.userRepository.update_user(id,body)
        if response>0:
            return response
        else:
            raise Exception("No se pudo modificar el usuario")
        
    def eliminar_usuario(self,id):
        current_app.logger.info("Service -> eliminar_usuario()")
        self.obtener_usuario_por_id(id)
        listaTareas = json_util.loads(self.obtener_listasTareas_por_user(id))
        response = self.userRepository.delete_user(id)
        for listaTarea in listaTareas:
            self.listaTareasService.eliminar_listaTareas(str(listaTarea['_id']))
        if response>0:
            return response
        else:
            raise Exception("No se pudo eliminar el usuario")
        
    def obtener_notas_por_user(self,id_user):
        current_app.logger.info("Service -> obtener_notas_por_user()")
        self.obtener_usuario_por_id(id_user)
        response = self.notaRepository.get_notes_by_user(id_user)
        return response
        
    def obtener_listasTareas_por_user(self,user_id):
        current_app.logger.info("Service -> obtener_listaTareas_por_user()")
        self.obtener_usuario_por_id(user_id)
        response = self.listaTareasRepo.get_listasTareas_by_user(user_id)
        return response
    
    def obtener_tareas_completadas(self,user_id):
        current_app.logger.info("Service -> obtener_tareas()")
        self.obtener_usuario_por_id(user_id)
        response = self.listaTareasRepo.get_tareas_completed(user_id)
        return response