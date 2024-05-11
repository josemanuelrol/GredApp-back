#Imports
from flask_pymongo import PyMongo
from flask import current_app
from bson import json_util
from bson import ObjectId

class UserRepository():
    
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db.usuarios

    def create_user(self,body):
        current_app.logger.info("DB -> create_user()")
        response = self.db.insert_one(body)
        return response.inserted_id
    
    def get_users(self):
        current_app.logger.info("DB -> get_users()")
        response = self.db.find()
        return response
    
    def get_user_by_id(self, id_user):
        current_app.logger.info("DB -> get_user_by_id()")
        response = self.db.find_one({'_id':ObjectId(id_user)})
        return response
    
    def update_user(self, id_user, body):
        current_app.logger.info("DB -> update_user()")
        response = self.db.update_one({'_id':ObjectId(id_user)}, {'$set': body})
        return response.modified_count
    
    def delete_user(self, id_user):
        current_app.logger.info("DB -> delete_user()")
        response = self.db.delete_one({'_id':ObjectId(id_user)})
        return response.deleted_count