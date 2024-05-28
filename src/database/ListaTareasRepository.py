#Imports
from flask_pymongo import PyMongo
from flask import current_app
from bson import json_util
from bson import ObjectId

class ListaTareasRepository():
    
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db.listaTareas

    def create_listaTareas(self, body):
        current_app.logger.info("DB -> create_listaTareas()")
        response = self.db.insert_one(body)
        return str(response.inserted_id)
    
    def get_all_listaTareas(self):
        current_app.logger.info("DB -> get_all_listaTareas()")
        response = self.db.find()
        return json_util.dumps(response)
    
    def get_listaTareas_by_id(self,id_lista):
        current_app.logger.info("DB -> get_listaTareas_by_id()")
        response = self.db.find_one({'_id':ObjectId(id_lista)})
        return json_util.dumps(response)
    
    def get_listasTareas_by_user(self,user_id):
        current_app.logger.info("DB -> get_listaTareas_by_user()")
        response = self.db.find({'user_id':user_id})
        return json_util.dumps(response)
    
    def update_listaTareas(self, id_lista, body):
        current_app.logger.info("DB -> update_listaTareas()")
        response = self.db.update_one({'_id':ObjectId(id_lista)},{'$set': body})
        return int(response.modified_count)
    
    def delete_listaTareas(self, id_lista):
        current_app.logger.info("DB -> delete_listaTareas()")
        response = self.db.delete_one({'_id':ObjectId(id_lista)})
        return int(response.deleted_count)
    
    #TAREAS

    def get_tareas(self, id_lista):
        current_app.logger.info("DB -> get_tareas()")
        response = self.db.find_one({'_id':ObjectId(id_lista)}, {'tareas':1, '_id':0})
        return json_util.dumps(response)
    
    def get_tareas_completed(self, user_id):
        current_app.logger.info("DB -> get_tareas_completed()")
        taskLists = self.db.find({'user_id':user_id})
        tasks = []
        for taskList in taskLists:
            for task in taskList['tareas']:
                if task['completed']:
                    tasks.append(task)
        return json_util.dumps(tasks)

    
    def get_tarea_by_id(self, id_lista, id_task):
        current_app.logger.info("DB -> get_tarea_by_id()")
        response = self.db.find_one({'_id':ObjectId(id_lista),'tareas':{'$elemMatch':{'_id':ObjectId(id_task)}}},{'tareas.$':1,'_id':0})
        return json_util.dumps(response)

    def add_tarea(self, id_lista, task):
        current_app.logger.info("DB -> add_tarea()")
        task['completed'] = False
        task['proridad'] = 0
        task['_id'] = ObjectId()
        response = self.db.update_one({'_id':ObjectId(id_lista)}, {'$push':{'tareas':task}})
        return int(response.modified_count)
    
    def update_tarea(self, id_lista, id_task, taskBody):
        current_app.logger.info("DB -> update_tarea()")
        actualizacion = {"$set": {}}
        for clave, valor in taskBody.items():
            actualizacion["$set"][f"tareas.$.{clave}"] = valor
        response = self.db.update_one({'_id':ObjectId(id_lista),'tareas._id':ObjectId(id_task)},actualizacion)
        return int(response.modified_count)

    def delete_tarea(self, id_lista, id_task):
        current_app.logger.info("DB -> delete_tarea()")
        response = self.db.update_one({'_id':ObjectId(id_lista)},{'$pull':{'tareas':{'_id':ObjectId(id_task)}}})
        return int(response.modified_count)
    