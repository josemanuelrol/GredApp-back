#Imports
from flask import current_app
from bson import json_util
from src.database.ListaTareasRepository import ListaTareasRepository
from src.models.ListaTareasNotFoundException import ListaTareasNotFoundException

class ListaTareasService():
    
    def __init__(self, listaTareaRepo:ListaTareasRepository):
        self.listaTareaRepo = listaTareaRepo

    def crear_listaTareas(self,body):
        current_app.logger.info("Service -> crear_listaTareas()")
        response = self.listaTareaRepo.create_listaTareas(body)
        if response != 'null':
            return response
        else:
            raise Exception("No se ha podido crear la lista de tareas")
        
    def obtener_listasTareas(self):
        current_app.logger.info("Service -> obtener_listasTareas()")
        response = self.listaTareaRepo.get_all_listaTareas()
        return response
    
    def obtener_listaTareas_por_id(self,id):
        current_app.logger.info("Service -> obtener_listaTareas_por_id()")
        response = self.listaTareaRepo.get_listaTareas_by_id(id)
        if response != 'null':
            return response
        else:
            raise ListaTareasNotFoundException()
        
    def modificar_listaTareas(self,id,body):
        current_app.logger.info("Service -> modificar_listaTareas()")
        self.obtener_listaTareas_por_id(id)
        response = self.listaTareaRepo.update_listaTareas(id,body)
        if response>0:
            return response
        else:
            raise Exception("No se pudo modificar la lista de tareas")
        
    def eliminar_listaTareas(self,id):
        current_app.logger.info("Service -> eliminar_listaTareas()")
        self.obtener_listaTareas_por_id(id)
        response = self.listaTareaRepo.delete_listaTareas(id)
        if response>0:
            return response
        else:
            raise Exception("No se pudo eliminar la lista de tareas")