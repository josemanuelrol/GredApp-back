#Imports
from flask import request, jsonify, Response, Blueprint

class NotaController():

    def __init__(self, notaService):
        self.api_bp = Blueprint('nota', __name__, url_prefix='/nota')
        self.notaService = notaService
        self.init_routes()

    def init_routes(self):
        pass
        #Aquí van los endpoints