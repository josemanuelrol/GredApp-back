#Imports
from bson import json_util

class ListaTareasService():
    
    def __init__(self, listaTareaRepo):
        self.listaTareaRepo = listaTareaRepo