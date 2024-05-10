#Imports
from bson import json_util

class EventoService():
    
    def __init__(self, eventoRepository):
        self.eventoRepository = eventoRepository