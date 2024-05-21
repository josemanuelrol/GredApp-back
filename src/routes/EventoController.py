#Imports
from flask import request, jsonify, Response, Blueprint, current_app
from src.services.EventoService import EventoService
from src.models.EventoNotFoundException import EventoNotFoundException

class EventoController():

    def __init__(self, eventoService:EventoService):
        self.api_bp = Blueprint('evento', __name__, url_prefix='/api')
        self.eventoService = eventoService
        self.init_routes()

    def init_routes(self):
        #Aquí van los endpoints

        @self.api_bp.route('/evento', methods=['POST'])
        def crear_evento():
            try:
                current_app.logger.info("API -> crear_evento()")
                body = request.get_json()
                response = self.eventoService.crear_evento(body)
                return jsonify({
                    'id':response,
                    'mensaje':'Evento creado'
                    })
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/eventos', methods=['GET'])
        def obtener_eventos():
            try:
                current_app.logger.info("API -> obtener_eventos()")
                response = self.eventoService.obtener_eventos()
                return Response(response, mimetype='application/json')
            except Exception as e:
                return jsonify({'error':str(e)}),404

        @self.api_bp.route('/evento/<id>', methods=['GET'])
        def obtener_evento_por_id(id):
            try:
                current_app.logger.info("API -> obtener_evento_por_id()")
                response = self.eventoService.obtener_evento_por_id(id)
                return Response(response, mimetype='application/json')
            except EventoNotFoundException as e:
                return jsonify({'error':str(e)}),404
            
        @self.api_bp.route('/evento/<id>', methods=['PUT'])
        def modificar_evento(id):
            try:
                current_app.logger.info("API -> modificar_evento()")
                body = request.get_json()
                self.eventoService.modificar_evento(id,body)
                return jsonify({'mensaje':'Evento modificado'})
            except EventoNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/evento/<id>', methods=['DELETE'])
        def eliminar_evento(id):
            try:
                current_app.logger.info("API -> eliminar_evento()")
                self.eventoService.eliminar_evento(id)
                return jsonify({'mensaje':'Evento eliminado'})
            except EventoNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400