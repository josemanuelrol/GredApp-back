#Imports
from bson import json_util

class NotaService():
    
    def __init__(self, notaRepository):
        self.notaRepository = notaRepository