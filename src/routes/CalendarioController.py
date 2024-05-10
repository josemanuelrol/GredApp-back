#Imports
from flask import request, jsonify, Response, Blueprint

class CalendarioController():

    def __init__(self, calendarioService):
        self.api_bp = Blueprint('calendario', __name__, url_prefix='/calendario')
        self.calendarioService = calendarioService
        self.init_routes()

    def init_routes(self):
        pass
        #Aquí van los endpoints