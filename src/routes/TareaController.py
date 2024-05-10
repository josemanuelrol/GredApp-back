#Imports
from flask import request, jsonify, Response, Blueprint

class TareaController():

    def __init__(self, tareaService):
        self.api_bp = Blueprint('tarea', __name__, url_prefix='/tarea')
        self.tareaService = tareaService
        self.init_routes()

    def init_routes(self):
        pass
        #Aquí van los endpoints