#Imports
from flask import request, jsonify, Response, Blueprint

class ListaTareasController():

    def __init__(self, listaTareasService):
        self.api_bp = Blueprint('listaTareas', __name__, url_prefix='/listaTareas')
        self.listaTareasService = listaTareasService
        self.init_routes()

    def init_routes(self):
        pass
        #Aquí van los endpoints