#Imports
from flask import current_app
from bson import json_util
from src.database.TareaRepository import TareaRepository
from src.models.TareaNotFoundException import TareaNotFoundException

class TareaService():
    
    def __init__(self, tareaRepository:TareaRepository):
        self.tareaRepository = tareaRepository

    def crear_tarea(self,body):
        current_app.logger.info("Service -> crear_tarea()")
        response = self.tareaRepository.create_task(body)
        if response != 'null':
            return response
        else:
            raise Exception("No se ha podido crear la tarea")
        
    def obtener_tareas(self):
        current_app.logger.info("Service -> obtener_tareas()")
        response = self.tareaRepository.get_all_tasks()
        return response
    
    def obtener_tarea_por_id(self,id):
        current_app.logger.info("Service -> obtener_tarea_por_id()")
        response = self.tareaRepository.get_task_by_id(id)
        if response != 'null':
            return response
        else:
            raise TareaNotFoundException()
        
    def modificar_tarea(self,id,body):
        current_app.logger.info("Service -> modificar_tarea()")
        self.obtener_tarea_por_id(id)
        response = self.tareaRepository.update_task(id,body)
        if response>0:
            return response
        else:
            raise Exception("No se pudo modificar la tarea")
        
    def eliminar_tarea(self,id):
        current_app.logger.info("Service -> eliminar_tarea()")
        self.obtener_tarea_por_id(id)
        response = self.tareaRepository.delete_task(id)
        if response>0:
            return response
        else:
            raise Exception("No se pudo eliminar la tarea")


