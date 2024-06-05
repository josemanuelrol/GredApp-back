#Imports
from flask_pymongo import PyMongo
from flask import current_app
from bson import json_util
from bson import ObjectId

class NotaRepository():
    
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db.notas

    def create_note(self,body):
        current_app.logger.info("DB -> create_note()")
        response = self.db.insert_one(body)
        return str(response.inserted_id)
    
    def get_all_notes(self):
        current_app.logger.info("DB -> get_all_notes()")
        response = self.db.find()
        return json_util.dumps(response)
    
    def get_note_by_id(self, id_note):
        current_app.logger.info("DB -> get_note_by_id()")
        response = self.db.find_one({'_id': ObjectId(id_note)})
        return json_util.dumps(response)
    
    def get_notes_by_user(self, id_user):
        current_app.logger.info("DB -> get_notes_by_user()")
        response = self.db.find({'user_id':id_user})
        return json_util.dumps(response)
    
    def update_note(self,id_note,body):
        current_app.logger.info("DB -> update_note()")
        response = self.db.update_one({'_id':ObjectId(id_note)},{'$set':body})
        return int(response.modified_count)
    
    def delete_note(self, id_note):
        current_app.logger.info("DB -> delete_note()")
        response = self.db.delete_one({'_id':ObjectId(id_note)})
        return int(response.deleted_count)