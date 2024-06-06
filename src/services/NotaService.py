#Imports
from flask import current_app
from src.database.NotaRepository import NotaRepository
from src.models.NotaNotFoundException import NotaNotFoundException

# Servicio encargado de comunicar el repositorio con el controlador de las notas y añadir validación en el proceso
class NotaService():
    
    # Constructor
    def __init__(self, notaRepository:NotaRepository):
        self.notaRepository = notaRepository

    # Método para crear una nota verificando que se ha creado correctamente
    def crear_nota(self,body):
        current_app.logger.info("Service -> crear_nota()")
        response = self.notaRepository.create_note(body)
        if response != 'null':
            return response
        else:
            raise Exception("No se ha podido crear la nota")
    
    # Método para obtener todas las notas que existen
    def obtener_notas(self):
        current_app.logger.info("Service -> obtener_notas()")
        response = self.notaRepository.get_all_notes()
        return response
    
    # Método para obtener una nota por su id verificando que esa nota exista
    def obtener_nota_por_id(self,id):
        current_app.logger.info("Service -> obtener_nota_por_id()")
        response = self.notaRepository.get_note_by_id(id)
        if response != 'null':
            return response
        else:
            raise NotaNotFoundException()

    # Método para modificar una nota verificando que dicha nota exista
    def modificar_nota(self,id,body):
        current_app.logger.info("Service -> modificar_nota()")
        self.obtener_nota_por_id(id)
        response = self.notaRepository.update_note(id,body)
        if response>0:
            return response
        else:
            raise Exception("No se pudo modificar la nota")
    
    # Método para eliminar una nota verificando que dicha nota exista
    def eliminar_nota(self,id):
        current_app.logger.info("Service -> eliminar_nota()")
        self.obtener_nota_por_id(id)
        response = self.notaRepository.delete_note(id)
        if response>0:
            return response
        else:
            raise Exception("No se pudo eliminar la nota")