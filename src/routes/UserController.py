#Imports
from flask import request, jsonify, Response, Blueprint, current_app

class UserController():

    def __init__(self, userService):
        self.api_bp = Blueprint('user', __name__, url_prefix='/user')
        self.userService = userService
        self.init_routes()

    def init_routes(self):
        pass
        #Aquí van los endpoints