#Imports
from flask import current_app
from bson import json_util
from src.database.EventoRepository import EventoRepository

class EventoService():
    
    def __init__(self, eventoRepository:EventoRepository):
        self.eventoRepository = eventoRepository

    def crear_evento(self,body):
        current_app.logger.info("Service -> crear_evento()")
        response = self.eventoRepository.create_event(body)
        if response != 'null':
            return response
        else:
            raise Exception("No se ha podido crear el evento")
        
    def obtener_eventos(self):
        current_app.logger.info("Service -> obtener_eventos()")
        response = self.eventoRepository.get_all_events()
        return response
    
    def obtener_evento_por_id(self,id):
        current_app.logger.info("Service -> obtener_evento_por_id()")
        response = self.eventoRepository.get_event_by_id(id)
        if response != 'null':
            return response
        else:
            raise Exception("Evento no encontrado")
        
    def modificar_evento(self,id,body):
        current_app.logger.info("Service -> modificar_evento()")
        response = self.eventoRepository.update_event(id,body)
        if response>0:
            return response
        else:
            raise Exception("Evento no encontrado")
        
    def eliminar_evento(self,id):
        current_app.logger.info("Service -> eliminar_evento()")
        response = self.eventoRepository.delete_event(id)
        if response>0:
            return response
        else:
            raise Exception("Evento no encontrado")