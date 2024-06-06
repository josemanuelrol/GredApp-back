#Imports
from flask import current_app
from src.database.EventoRepository import EventoRepository
from src.services.UserService import UserService
from src.models.EventoNotFoundException import EventoNotFoundException

# Servicio de los eventos encargado de comunicar el controlador con el repositorio y añade validación en el proceso.
class EventoService():
    
    # Constructor
    def __init__(self, eventoRepository:EventoRepository, userService:UserService):
        self.eventoRepository = eventoRepository
        self.userService = userService

    # Método para crear un evento comprobando si se ha creado correctamente o no.
    def crear_evento(self,body):
        current_app.logger.info("Service -> crear_evento()")
        response = self.eventoRepository.create_event(body)
        if response != 'null':
            return response
        else:
            raise Exception("No se ha podido crear el evento")
    
    # Método para obtener todos los eventos
    def obtener_eventos(self):
        current_app.logger.info("Service -> obtener_eventos()")
        response = self.eventoRepository.get_all_events()
        return response
    
    # Método para obtener todos los eventos del usuario comprobando previamente que exista dicho usuario
    def obtener_eventos_por_usuario(self,user_id):
        current_app.logger.info("Service -> obtener_eventos_por_usuario()")
        self.userService.obtener_usuario_por_id(user_id)
        response = self.eventoRepository.get_all_events_by_user(user_id)
        return response
    
    # Método para obtener un evento por id comprobando que el evento exista
    def obtener_evento_por_id(self,id):
        current_app.logger.info("Service -> obtener_evento_por_id()")
        response = self.eventoRepository.get_event_by_id(id)
        if response != 'null':
            return response
        else:
            raise EventoNotFoundException()
        
    # Método para modificar un evento comprobando que el evento existe y si se ha modificado correctamente
    def modificar_evento(self,id,body):
        current_app.logger.info("Service -> modificar_evento()")
        self.obtener_evento_por_id(id)
        response = self.eventoRepository.update_event(id,body)
        if response>0:
            return response
        else:
            raise Exception("No se pudo modificar el evento")
        
    # Método para eliminar un evento comprobando que exista
    def eliminar_evento(self,id):
        current_app.logger.info("Service -> eliminar_evento()")
        self.obtener_evento_por_id(id)
        response = self.eventoRepository.delete_event(id)
        if response>0:
            return response
        else:
            raise Exception("No se pudo eliminar el evento")