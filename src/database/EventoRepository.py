#Imports
from flask_pymongo import PyMongo
from flask import current_app
from bson import json_util
from bson import ObjectId

# Clase repositorio que se encarga de la comunicación con la base de datos para gestionar la colección de eventos.
class EventoRepository():
    
    # Constructor
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db.eventos

    # Método para crear un evento
    def create_event(self, body):
        current_app.logger.info("DB -> create_event()")
        response = self.db.insert_one(body)
        return str(response.inserted_id)
    
    # Método que obtiene todos los eventos de la colección
    def get_all_events(self):
        current_app.logger.info("DB -> get_all_events()")
        response = self.db.find()
        return json_util.dumps(response)
    
    # Método que obtiene todos los eventos del usuario con el id que se pasa como parámetro
    def get_all_events_by_user(self, user_id):
        current_app.logger.info("DB -> get_all_events_by_user()")
        response = self.db.find({'user_id':user_id})
        return json_util.dumps(response)
    
    # Método para obtener un evento según su id
    def get_event_by_id(self, id_event):
        current_app.logger.info("DB -> get_event_by_id()")
        response = self.db.find_one({'_id': ObjectId(id_event)})
        return json_util.dumps(response)
    
    # Método para modifiar las propiedades de un evento
    def update_event(self, id_event, body):
        current_app.logger.info("DB -> update_event()")
        response = self.db.update_one({'_id':ObjectId(id_event)},{'$set': body})
        return int(response.modified_count)
    
    # Método para eliminar un evento
    def delete_event(self, id_event):
        current_app.logger.info("DB -> delete_event()")
        response = self.db.delete_one({'_id':ObjectId(id_event)})
        return int(response.deleted_count)