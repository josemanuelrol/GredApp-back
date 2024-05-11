#Imports
from flask_pymongo import PyMongo
from flask import current_app
from bson import json_util
from bson import ObjectId

class TareaRepository():
    
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db.tareas

    def create_task(self, body):
        current_app.logger.info("DB -> create_task()")
        response = self.db.insert_one(body)
        return response.inserted_id
    
    def get_all_tasks(self):
        current_app.logger.info("DB -> get_all_tasks()")
        response = self.db.find()
        return response
    
    def get_task_by_id(self, id_task):
        current_app.logger.info("DB -> get_task_by_id()")
        response = self.db.find_one({'_id':ObjectId(id_task)})
        return response
    
    def update_task(self, id_task, body):
        current_app.logger.info("DB -> update_task()")
        response = self.db.update_one({'_id':ObjectId(id_task)},{'$set':body})
        return response.modified_count
    
    def delete_task(self, id_task):
        current_app.logger.info("DB -> delete_task()")
        response = self.db.delete_one({'_id':ObjectId(id_task)})
        return response.deleted_count