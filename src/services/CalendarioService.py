#Imports
from bson import json_util

class CalendarioService():
    
    def __init__(self, calendarioRepository):
        self.calendarioRepository = calendarioRepository
        
