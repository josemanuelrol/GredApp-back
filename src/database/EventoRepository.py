#Imports
from flask_pymongo import PyMongo
from flask import current_app
from bson import json_util
from bson import ObjectId

class EventoRepository():
    
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db.eventos

    def create_event(self, body):
        current_app.logger.info("DB -> create_event()")
        response = self.db.insert_one(body)
        return response.inserted_id
    
    def get_all_events(self):
        current_app.logger.info("DB -> get_all_events()")
        response = self.db.find()
        return response
    
    def get_event_by_id(self, id_event):
        current_app.logger.info("DB -> get_event_by_id()")
        response = self.db.find_one({'_id': ObjectId(id_event)})
        return response
    
    def update_event(self, id_event, body):
        current_app.logger.info("DB -> update_event()")
        response = self.db.update_one({'_id':ObjectId(id_event)},{'$set': body})
        return response.modified_count
    
    def delete_event(self, id_event):
        current_app.logger.info("DB -> delete_event()")
        response = self.db.delete_one({'_id':ObjectId(id_event)})
        return response.deleted_count