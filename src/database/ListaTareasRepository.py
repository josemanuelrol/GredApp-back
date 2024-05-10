#Imports
from flask_pymongo import PyMongo
from bson import json_util
from bson import ObjectId

class ListaTareasRepository():
    
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db.listaTareas