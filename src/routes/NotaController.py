#Imports
from flask import request, jsonify, Response, Blueprint, current_app
from src.services.NotaService import NotaService

class NotaController():

    def __init__(self, notaService:NotaService):
        self.api_bp = Blueprint('nota', __name__, url_prefix='/api')
        self.notaService = notaService
        self.init_routes()

    def init_routes(self):
        #Aquí van los endpoints

        @self.api_bp.route('/nota', methods=['POST'])
        def crear_nota():
            try:
                current_app.logger.info("API -> crear_nota()")
                body = request.get_json()
                response = self.notaService.crear_nota(body)
                return jsonify({
                    'id':response,
                    'mensaje':'Nota creada'
                    })
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/notas', methods=['GET'])
        def obtener_notas():
            current_app.logger.info("API -> obtener_notas()")
            response = self.notaService.obtener_notas()
            return Response(response,mimetype='application/json')
        
        @self.api_bp.route('/nota/<id>', methods=['GET'])
        def obtener_nota_por_id(id):
            try:
                current_app.logger.info("API -> obtener_nota_por_id()")
                response = self.notaService.obtener_nota_por_id(id)
                return Response(response, mimetype='application/json')
            except Exception as e:
                return jsonify({'error':str(e)}),404
            
        @self.api_bp.route('/nota/<id>', methods=['PUT'])
        def modificar_nota(id):
            try:
                current_app.logger.info("API -> modificar_nota()")
                body = request.get_json()
                self.notaService.modificar_nota(id,body)
                return jsonify({'mensaje':'Nota modificada'})
            except Exception as e:
                return jsonify({'error':str(e)}),404
            
        @self.api_bp.route('/nota/<id>', methods=['DELETE'])
        def eliminar_nota(id):
            try:
                current_app.logger.info("API -> eliminar_nota()")
                self.notaService.eliminar_nota(id)
                return jsonify({'mensaje':'Nota eliminada'})
            except Exception as e:
                return jsonify({'error':str(e)})
