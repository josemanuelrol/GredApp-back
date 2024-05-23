#Imports
from flask import request, jsonify, Response, Blueprint, current_app
from src.services.CalendarioService import CalendarioService
from src.models.CalendarioNotFoundException import CalendarioNotFoundException

class CalendarioController():

    def __init__(self, calendarioService:CalendarioService):
        self.api_bp = Blueprint('calendario', __name__, url_prefix='/api')
        self.calendarioService = calendarioService
        self.init_routes()

    def init_routes(self):
        #Aquí van los endpoints

        @self.api_bp.route('/calendario', methods=['POST'])
        def crear_calendario():
            try:
                current_app.logger.info("API -> crear_calendario()")
                body = request.get_json()
                response = self.calendarioService.crear_calendario(body)
                return jsonify({
                    'id':response,
                    'mensaje':'Calendario creado'
                    })
            except Exception as e:
                return jsonify({'error': str(e)}),400
            
        @self.api_bp.route('/calendarios', methods=['GET'])
        def obtener_calendarios():
            current_app.logger.info("API -> obtener_calendarios()")
            response = self.calendarioService.obtener_calendarios()
            return Response(response, mimetype='application/json')
            
        @self.api_bp.route('/calendario/<id>', methods=['GET'])
        def obtener_calendario_por_id(id):
            try:
                current_app.logger.info("API -> obtener_calendario_por_id()")
                response = self.calendarioService.obtener_calendario_por_id(id)
                return Response(response, mimetype='application/json')
            except CalendarioNotFoundException as e:
                return jsonify({'error':str(e)}),404
            
        @self.api_bp.route('/calendario/<id>', methods=['PUT'])
        def modificar_calendario(id):
            try:
                current_app.logger.info("API -> modificar_calendario()")
                body = request.get_json()
                self.calendarioService.modificar_calendario(id,body)
                return jsonify({'mensaje':'Calendario modificado'})
            except CalendarioNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/calendario/<id>', methods=['DELETE'])
        def eliminar_caledario(id):
            try:
                current_app.logger.info("API -> eliminar_calendario()")
                self.calendarioService.eliminar_calendario(id)
                return jsonify({'mensaje':'Calendario eliminado'})
            except CalendarioNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
