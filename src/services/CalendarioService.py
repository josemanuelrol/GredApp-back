#Imports
from flask import current_app
from src.database.CalendarioRepository import CalendarioRepository
from src.models.CalendarioNotFoundException import CalendarioNotFoundException

class CalendarioService():
    
    def __init__(self, calendarioRepository:CalendarioRepository):
        self.calendarioRepository = calendarioRepository

    def crear_calendario(self,body):
        current_app.logger.info("Service -> crear_calendario()")
        response = self.calendarioRepository.create_calendar(body)
        if response != 'null':
            return response
        else:
            raise Exception("No se ha podido crear el calendario")
        
    def obtener_calendarios(self):
        current_app.logger.info("Service -> obtener_calendarios()")
        response = self.calendarioRepository.get_all_calendars()
        if response != '[]':
            return response
        else:
            raise Exception("No existen calendarios")
    
    def obtener_calendario_por_id(self,id):
        current_app.logger.info("Service -> obtener_calendario_por_id()")
        response = self.calendarioRepository.get_calendar_by_id(id)
        if response != 'null' :
            return response
        else:
            raise CalendarioNotFoundException()
        
    def modificar_calendario(self,id,body):
        current_app.logger.info("Service -> modificar_calendario()")
        self.obtener_calendario_por_id(id)
        response = self.calendarioRepository.update_calendar(id,body)
        if response>0:
            return response
        else:
            raise Exception("No se pudo modificar el calendario")
        
    def eliminar_calendario(self,id):
        current_app.logger.info("Service -> eliminar_calendario()")
        self.obtener_calendario_por_id(id)
        response = self.calendarioRepository.delete_calendar(id)
        if response>0:
            return response
        else:
            raise Exception("No se pudo eliminar el calendario")
        
