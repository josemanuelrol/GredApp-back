#Imports
from flask import current_app
from bson import json_util
from src.database.ListaTareasRepository import ListaTareasRepository
from src.models.ListaTareasNotFoundException import ListaTareasNotFoundException
from src.models.TareaNotFoundException import TareaNotFoundException

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
        if response != '[]':
            return response
        else:
            raise Exception("No existen listas de tareas")
    
    def obtener_listaTareas_por_id(self,id):
        current_app.logger.info("Service -> obtener_listaTareas_por_id()")
        response = self.listaTareaRepo.get_listaTareas_by_id(id)
        if response != 'null':
            return response
        else:
            raise ListaTareasNotFoundException()
        
    def modificar_listaTareas(self,id,id_task):
        current_app.logger.info("Service -> modificar_listaTareas()")
        self.obtener_listaTareas_por_id(id)
        response = self.listaTareaRepo.update_listaTareas(id,id_task)
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
        
    #TAREAS

    def obtener_tareas(self,id_lista):
        current_app.logger.info("Service -> obtener_tareas()")
        self.obtener_listaTareas_por_id(id_lista)
        response = self.listaTareaRepo.get_tareas(id_lista)
        return response
        
    def obtener_tarea_por_id(self,id_lista,id_task):
        current_app.logger.info("Service -> obtener_tarea_por_id()")
        self.obtener_listaTareas_por_id(id_lista)
        response = self.listaTareaRepo.get_tarea_by_id(id_lista, id_task)
        if response != 'null':
            tareas = json_util.loads(response)
            return json_util.dumps(tareas['tareas'][0])
        else:
            raise TareaNotFoundException()

    def aniadir_tarea(self,id_lista,task):
        current_app.logger.info("Service -> aniadir_tarea()")
        self.obtener_listaTareas_por_id(id_lista)
        response = self.listaTareaRepo.add_tarea(id_lista, task)
        if response>0:
            return response
        else:
            raise Exception("No se pudo añadir la tarea")
        
    def modificar_tarea(self, id_lista, id_task, taskBody):
        current_app.logger.info("Service -> modificar_tarea()")
        self.obtener_listaTareas_por_id(id_lista)
        self.obtener_tarea_por_id(id_lista, id_task)
        response = self.listaTareaRepo.update_tarea(id_lista,id_task,taskBody)
        if response>0:
            return response
        else:
            raise Exception("No se pudo modificar la tarea")
        
    def eliminar_tarea(self,id_lista,task):
        current_app.logger.info("Service -> eliminar_tarea()")
        self.obtener_listaTareas_por_id(id_lista)
        response = self.listaTareaRepo.delete_tarea(id_lista, task)
        if response>0:
            return response
        else:
            raise Exception("No se pudo eliminar la tarea")
        