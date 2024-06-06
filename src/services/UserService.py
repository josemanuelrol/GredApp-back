#Imports
from flask import current_app
from bson import json_util
from src.database.UserRepository import UserRepository
from src.database.NotaRepository import NotaRepository
from src.services.ListaTareasService import ListaTareasService
from src.database.ListaTareasRepository import ListaTareasRepository
from src.models.UserNotFoundException import UserNotFoundException

# Servicio encargado de conectar el repositorio con el controlador de los usuarios y añadiendo validación en el proceso
class UserService():
    
    # Constructor
    def __init__(self, userRepository:UserRepository, listaTareasService:ListaTareasService, notaRepository:NotaRepository, 
                 listaTareasRepo:ListaTareasRepository):
        self.userRepository = userRepository
        self.listaTareasService = listaTareasService
        self.notaRepository = notaRepository
        self.listaTareasRepo = listaTareasRepo

    # Método para crear un usuario comprobando que no exista un usuario con el mismo nombre de usuario y creando una lista de tareas por defecto del usuario.
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

    # Método para cambiar la contraseña verificando que se ha modificado correctamente
    def cambiar_contraseña(self,user_id,new_password):
        current_app.logger.info("Service -> cambiar_contraseña()")
        response = self.userRepository.change_password(user_id, new_password)
        if response > 0:
            return response
        else:
            raise Exception("No se pudo cambiar la contraseña")

    # Método para obtener todos los usuarios.
    def obtener_usuarios(self):
        current_app.logger.info("Services -> obtener_usuarios()")
        response = self.userRepository.get_users()
        return response
    
    # Método para obtener un usuario por su nombre de usuario y verificando si el usuario se ha encontrado
    def obtener_usuario_por_username(self,username):
        current_app.logger.info("Service -> obtener_usuario_por_username()")
        response = self.userRepository.get_user_by_username(username)
        if response != 'null':
            return response
        else:
            raise UserNotFoundException()
    
    # Método para obtener un usuario por su id verificando si el usuario se ha encontrado
    def obtener_usuario_por_id(self, id):
        current_app.logger.info("Service -> obtener_usuario_por_id()")
        response = self.userRepository.get_user_by_id(id)
        if response != 'null':
            return response
        else:
            raise UserNotFoundException()
    
    # Método para modificar un usuario verificando que el usuario existe y que se ha modificado correctamente
    def modificar_usuario(self,id,body):
        current_app.logger.info("Service -> modificar_usuario()")
        self.obtener_usuario_por_id(id)
        response = self.userRepository.update_user(id,body)
        if response>0:
            return response
        else:
            raise Exception("No se pudo modificar el usuario")

    # Método para eliminar un usuario verificando que el usuario existe y que se ha eliminado correctamente  
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
        
    # Método para obtener todas las notas del usuario verificando que el usuario existe
    def obtener_notas_por_user(self,id_user):
        current_app.logger.info("Service -> obtener_notas_por_user()")
        self.obtener_usuario_por_id(id_user)
        response = self.notaRepository.get_notes_by_user(id_user)
        return response
        
    # Método para obtener todas las listas de tareas del usuario verificando que el usuario existe
    def obtener_listasTareas_por_user(self,user_id):
        current_app.logger.info("Service -> obtener_listaTareas_por_user()")
        self.obtener_usuario_por_id(user_id)
        response = self.listaTareasRepo.get_listasTareas_by_user(user_id)
        return response
    
    # Método para obtener todas las tareas completadas del usuario verificando que el usuario existe
    def obtener_tareas_completadas(self,user_id):
        current_app.logger.info("Service -> obtener_tareas()")
        self.obtener_usuario_por_id(user_id)
        response = self.listaTareasRepo.get_tareas_completed(user_id)
        return response