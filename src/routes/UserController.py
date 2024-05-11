#Imports
from flask import request, jsonify, Response, Blueprint, current_app
from src.services.UserService import UserService

class UserController():

    def __init__(self, userService:UserService):
        self.api_bp = Blueprint('user', __name__, url_prefix='/api')
        self.userService = userService
        self.init_routes()

    def init_routes(self):
        #Aquí van los endpoints

        @self.api_bp.route('/user', methods=['POST'])
        def crear_usuario():
            try:
                current_app.logger.info("API -> crear_usuario()")
                body = request.get_json()
                response = self.userService.crear_usuario(body)
                return jsonify({
                    'id':response,
                    'mensaje':'Usuario creado'
                    })
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/users', methods=['GET'])
        def obtener_usuarios():
            current_app.logger.info("API -> obtener_usuarios()")
            response = self.userService.obtener_usuarios()
            return Response(response,mimetype='application/json')
        
        @self.api_bp.route('/user/<id>', methods=['GET'])
        def obtener_usuario_por_id(id):
            try:
                current_app.logger.info("API -> obtener_usuario_por_id()")
                response = self.userService.obtener_usuario_por_id(id)
                return Response(response, mimetype='application/json')
            except Exception as e:
                return jsonify({'error':str(e)}),404
            
        @self.api_bp.route('/user/<id>', methods=['PUT'])
        def modificar_usuario(id):
            try:
                current_app.logger.info("API -> modificar_usuario()")
                body = request.get_json()
                self.userService.modificar_usuario(id,body)
                return jsonify({'mensaje':'Usuario modificado'})
            except Exception as e:
                return jsonify({'error':str(e)}),404
            
        @self.api_bp.route('/user/<id>', methods=['DELETE'])
        def eliminar_usuario(id):
            try:
                current_app.logger.info("API -> eliminar_usuario()")
                self.userService.eliminar_usuario(id)
                return jsonify({'mensaje':'Usuario eliminado'})
            except Exception as e:
                return jsonify({'error':str(e)})