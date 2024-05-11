#Imports
from flask_pymongo import PyMongo
from flask import current_app
from bson import json_util
from bson import ObjectId

class CalendarioRepository():
    
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db.calendarios

    def create_calendar(self, body):
        current_app.logger.info("DB -> create_calendar()")
        response = self.db.insert_one(body)
        return response.inserted_id
    
    def get_all_calendars(self):
        current_app.logger.info("DB -> get_all_calendars()")
        response = self.db.find()
        return response
    
    def get_calendar_by_id(self,id_calendar):
        current_app.logger.info("DB -> get_calendar_by_id()")
        response = self.db.find_one({'_id':ObjectId(id_calendar)})
        return response
    
    def update_calendar(self,id_calendar, body):
        current_app.logger.info("DB -> update_calendar()")
        response = self.db.update_one({'_id':ObjectId(id_calendar)}, {'$set': body})
        return response.modified_count
    
    def delete_calendar(self, id_calendar):
        current_app.logger.info("DB -> delete_calendar()")
        response = self.db.delete_one({'_id':ObjectId(id_calendar)})
        return response.deleted_count