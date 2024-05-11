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
        return response.inserted_id
    
    def get_all_listaTareas(self):
        current_app.logger.info("DB -> get_all_listaTareas()")
        response = self.db.find()
        return response
    
    def get_listaTareas_by_id(self,id_lista):
        current_app.logger.info("DB -> get_listaTareas_by_id()")
        response = self.db.find_one({'_id':ObjectId(id_lista)})
        return response
    
    def update_listaTareas(self, id_lista, body):
        current_app.logger.info("DB -> update_listaTareas()")
        response = self.db.update_one({'_id':ObjectId(id_lista)},{'$set': body})
        return response.modified_count
    
    def delete_listaTareas(self, id_lista):
        current_app.logger.info("DB -> delete_listaTareas()")
        response = self.db.delete_one({'_id':ObjectId(id_lista)})
        return response.deleted_count
    