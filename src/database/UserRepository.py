#Imports
from flask_pymongo import PyMongo
from flask import current_app
from bson import json_util
from bson import ObjectId
import bcrypt

# Clase repositorio que se encarga de la comunicación con la base de datos para gestionar los usuarios
class UserRepository():
    
    # Constructor
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db.usuarios

    # Método que crea un usuario encriptando su contraseña para guardarla en base de datos.
    def create_user(self,body):
        current_app.logger.info("DB -> create_user()")

        password = body['password']

        encrypted_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        body['password'] = encrypted_password.decode('utf-8')
        
        response = self.db.insert_one(body)
        
        return str(response.inserted_id)
    
    # Método para cambiar la contraseña de un usuario encriptandola.
    def change_password(self,user_id, new_password):
        current_app.logger.info("DB -> change_password()")
        
        encrypted_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

        new_password = encrypted_password.decode('utf-8')

        body = {
            'password':new_password
        }

        return self.update_user(user_id, body)
    
    # Método para obtener todos los usuarios que existen
    def get_users(self):
        current_app.logger.info("DB -> get_users()")
        response = self.db.find()
        return json_util.dumps(response)
    
    # Método para obtener un usuario según su nombre de usuario
    def get_user_by_username(self,username):
        current_app.logger.info("DB -> get_user_by_username()")
        response = self.db.find_one({'username':username})
        return json_util.dumps(response)
    
    # Método que obtiene un usuario según su id.
    def get_user_by_id(self, id_user):
        current_app.logger.info("DB -> get_user_by_id()")
        response = self.db.find_one({'_id':ObjectId(id_user)})
        return json_util.dumps(response)
    
    # Método que modifica los parámetros de un usuario
    def update_user(self, id_user, body):
        current_app.logger.info("DB -> update_user()")
        response = self.db.update_one({'_id':ObjectId(id_user)}, {'$set': body})
        return int(response.modified_count)
    
    # Método que elimina un usuario
    def delete_user(self, id_user):
        current_app.logger.info("DB -> delete_user()")
        response = self.db.delete_one({'_id':ObjectId(id_user)})
        return int(response.deleted_count)