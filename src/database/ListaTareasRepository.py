#Imports
from flask_pymongo import PyMongo
from flask import current_app
from bson import json_util
from bson import ObjectId

# Clase repositorio que se encarga de la comunicación con la base de datos para gestionar las listas de tareas
class ListaTareasRepository():
    
    # Constructor
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db.listaTareas

    # Método para crear una nueva lista de tareas
    def create_listaTareas(self, body):
        current_app.logger.info("DB -> create_listaTareas()")
        response = self.db.insert_one(body)
        return str(response.inserted_id)
    
    # Método para obtener todas las listas de tareas existentes
    def get_all_listaTareas(self):
        current_app.logger.info("DB -> get_all_listaTareas()")
        response = self.db.find()
        return json_util.dumps(response)
    
    # Método para obtener una lista de tareas por su id
    def get_listaTareas_by_id(self,id_lista):
        current_app.logger.info("DB -> get_listaTareas_by_id()")
        response = self.db.find_one({'_id':ObjectId(id_lista)})
        return json_util.dumps(response)
    
    # Método para obtener las listas de tareas que posee un usuario según su id
    def get_listasTareas_by_user(self,user_id):
        current_app.logger.info("DB -> get_listaTareas_by_user()")
        response = self.db.find({'user_id':user_id})
        return json_util.dumps(response)
    
    # Método para modificar los parámetros de una lista de tareas
    def update_listaTareas(self, id_lista, body):
        current_app.logger.info("DB -> update_listaTareas()")
        response = self.db.update_one({'_id':ObjectId(id_lista)},{'$set': body})
        return int(response.modified_count)
    
    # Método para eliminar una lista de tareas
    def delete_listaTareas(self, id_lista):
        current_app.logger.info("DB -> delete_listaTareas()")
        response = self.db.delete_one({'_id':ObjectId(id_lista)})
        return int(response.deleted_count)
    
    #TAREAS

    # Método para obtener todas las tareas de una lista de tareas
    def get_tareas(self, id_lista):
        current_app.logger.info("DB -> get_tareas()")
        response = self.db.find_one({'_id':ObjectId(id_lista)}, {'tareas':1, '_id':0})
        return json_util.dumps(response)
    
    # Método que obtiene todas las tareas completadas de un usuario según su id
    def get_tareas_completed(self, user_id):
        current_app.logger.info("DB -> get_tareas_completed()")
        # Obtenemos las listas de tareas del usuario
        taskLists = self.db.find({'user_id':user_id})
        tasks = []
        # Recorremos cada lista de tareas obteniendo las tareas que tienen comprobando que cada tarea esté completada.
        for taskList in taskLists:
            for task in taskList['tareas']:
                if task['completed']:
                    tasks.append(task)
        # Devolvemos el array con las tareas completadas
        return json_util.dumps(tasks)
    
    # Método para obtener una tarea de una lista según su id
    def get_tarea_by_id(self, id_lista, id_task):
        current_app.logger.info("DB -> get_tarea_by_id()")
        response = self.db.find_one({'_id':ObjectId(id_lista),'tareas':{'$elemMatch':{'_id':ObjectId(id_task)}}},{'tareas.$':1,'_id':0})
        return json_util.dumps(response)

    # Método para crear una tarea en la lista indicada por id
    def add_tarea(self, id_lista, task):
        current_app.logger.info("DB -> add_tarea()")
        task['completed'] = False
        task['_id'] = ObjectId()
        response = self.db.update_one({'_id':ObjectId(id_lista)}, {'$push':{'tareas':task}})
        return int(response.modified_count)
    
    # Método para modificar una tarea de una lista según su id
    def update_tarea(self, id_lista, id_task, taskBody):
        current_app.logger.info("DB -> update_tarea()")
        actualizacion = {"$set": {}}
        for clave, valor in taskBody.items():
            actualizacion["$set"][f"tareas.$.{clave}"] = valor
        response = self.db.update_one({'_id':ObjectId(id_lista),'tareas._id':ObjectId(id_task)},actualizacion)
        return int(response.modified_count)

    # Método para eliminar una tarea de una lista según su id
    def delete_tarea(self, id_lista, id_task):
        current_app.logger.info("DB -> delete_tarea()")
        response = self.db.update_one({'_id':ObjectId(id_lista)},{'$pull':{'tareas':{'_id':ObjectId(id_task)}}})
        return int(response.modified_count)
    