#Imports
from flask import request, jsonify, Response, Blueprint, current_app
from src.services.NotaService import NotaService
from src.models.NotaNotFoundException import NotaNotFoundException

# Controlador que contiene los Endpoints y el tratamiento de los errores para las notas
class NotaController():

    # Constructor
    def __init__(self, notaService:NotaService):
        self.api_bp = Blueprint('nota', __name__, url_prefix='/api')
        self.notaService = notaService
        self.init_routes()

    # Método que inicializa todos los Endpoints del controlador
    def init_routes(self):
        #Aquí van los endpoints

        # Endpoint encargado de crear una nueva nota
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

        # Endpoint encargado de obtener todas las notas que existan  
        @self.api_bp.route('/notas', methods=['GET'])
        def obtener_notas():
            current_app.logger.info("API -> obtener_notas()")
            response = self.notaService.obtener_notas()
            return Response(response,mimetype='application/json')

        # Endpoint encargado de obtener una nota por su id
        @self.api_bp.route('/nota/<id>', methods=['GET'])
        def obtener_nota_por_id(id):
            try:
                current_app.logger.info("API -> obtener_nota_por_id()")
                response = self.notaService.obtener_nota_por_id(id)
                return Response(response, mimetype='application/json')
            except NotaNotFoundException as e:
                return jsonify({'error':str(e)}),404

        # Endpoint encargado de modificar una nota indicando su id 
        @self.api_bp.route('/nota/<id>', methods=['PUT'])
        def modificar_nota(id):
            try:
                current_app.logger.info("API -> modificar_nota()")
                body = request.get_json()
                self.notaService.modificar_nota(id,body)
                return jsonify({'mensaje':'Nota modificada'})
            except NotaNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
        
        # Endpoint encargado de eliminar una nota por su id
        @self.api_bp.route('/nota/<id>', methods=['DELETE'])
        def eliminar_nota(id):
            try:
                current_app.logger.info("API -> eliminar_nota()")
                self.notaService.eliminar_nota(id)
                return jsonify({'mensaje':'Nota eliminada'})
            except NotaNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
