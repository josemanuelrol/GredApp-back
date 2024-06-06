#Imports
from flask_pymongo import PyMongo
from flask import current_app
from bson import json_util
from bson import ObjectId

# Clase repositorio que se encarga de la comunicación con la base de datos para gestionar las notas.
class NotaRepository():
    
    # Constructor
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db.notas

    # Método para crear una nueva nota
    def create_note(self,body):
        current_app.logger.info("DB -> create_note()")
        response = self.db.insert_one(body)
        return str(response.inserted_id)
    
    # Método para obtener todas las notas que existen
    def get_all_notes(self):
        current_app.logger.info("DB -> get_all_notes()")
        response = self.db.find()
        return json_util.dumps(response)
    
    # Método para obtener un nota según su id
    def get_note_by_id(self, id_note):
        current_app.logger.info("DB -> get_note_by_id()")
        response = self.db.find_one({'_id': ObjectId(id_note)})
        return json_util.dumps(response)
    
    # Método para obtener las notas de un usuario según su id
    def get_notes_by_user(self, id_user):
        current_app.logger.info("DB -> get_notes_by_user()")
        response = self.db.find({'user_id':id_user})
        return json_util.dumps(response)
    
    # Método para modificar las propiedades de una nota
    def update_note(self,id_note,body):
        current_app.logger.info("DB -> update_note()")
        response = self.db.update_one({'_id':ObjectId(id_note)},{'$set':body})
        return int(response.modified_count)
    
    # Método para eliminar una nota.
    def delete_note(self, id_note):
        current_app.logger.info("DB -> delete_note()")
        response = self.db.delete_one({'_id':ObjectId(id_note)})
        return int(response.deleted_count)