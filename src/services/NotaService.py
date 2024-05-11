#Imports
from flask import current_app
from bson import json_util
from src.database.NotaRepository import NotaRepository

class NotaService():
    
    def __init__(self, notaRepository:NotaRepository):
        self.notaRepository = notaRepository

    def crear_nota(self,body):
        current_app.logger.info("Service -> crear_nota()")
        response = self.notaRepository.create_note(body)
        if response:
            return response
        else:
            raise Exception("No se ha podido crear la nota")
        
    def obtener_notas(self):
        current_app.logger.info("Service -> obtener_notas()")
        response = self.notaRepository.get_all_notes()
        return response
    
    def obtener_nota_por_id(self,id):
        current_app.logger.info("Service -> obtener_nota_por_id()")
        response = self.notaRepository.get_note_by_id(id)
        if response:
            return response
        else:
            raise Exception("Nota no encontrada")
        
    def modificar_nota(self,id,body):
        current_app.logger.info("Service -> modificar_nota()")
        response = self.notaRepository.update_note(id,body)
        if response>0:
            return response
        else:
            raise Exception("No se ha podido modificar la nota")
        
    def eliminar_nota(self,id):
        current_app.logger.info("Service -> eliminar_nota()")
        response = self.notaRepository.delete_note(id)
        if response>0:
            return response
        else:
            raise Exception("No se ha podido eliminar la nota")