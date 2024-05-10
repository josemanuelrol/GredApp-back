#Imports
from flask import request, jsonify, Response, Blueprint

class EventoController():

    def __init__(self, eventoService):
        self.api_bp = Blueprint('evento', __name__, url_prefix='/evento')
        self.eventoService = eventoService
        self.init_routes()

    def init_routes(self):
        pass
        #Aquí van los endpoints