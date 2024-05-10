#Imports
from bson import json_util

class TareaService():
    
    def __init__(self, tareaRepository):
        self.tareaRepository = tareaRepository