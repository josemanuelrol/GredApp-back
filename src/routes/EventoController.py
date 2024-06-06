#Imports
from flask import request, jsonify, Response, Blueprint, current_app
from src.services.EventoService import EventoService
from src.models.EventoNotFoundException import EventoNotFoundException

# Controlador que contiene los Endpoints y el tratamiento de los errores para los eventos
class EventoController():

    # Constructor
    def __init__(self, eventoService:EventoService):
        self.api_bp = Blueprint('evento', __name__, url_prefix='/api')
        self.eventoService = eventoService
        self.init_routes()

    # Método que inicializa todos los Endpoints del controlador
    def init_routes(self):
        #Aquí van los endpoints

        # Endpoint que recibe la petición para crear un evento
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
        
        # Endpoint que recibe la petición para obtener todos los eventos que existen
        @self.api_bp.route('/eventos', methods=['GET'])
        def obtener_eventos():
            current_app.logger.info("API -> obtener_eventos()")
            response = self.eventoService.obtener_eventos()
            return Response(response, mimetype='application/json')

        # Endpoint que recibe la petición para obtener todos los eventos de un usuario
        @self.api_bp.route('/user/<id>/eventos',methods=['GET'])
        def obtener_eventos_usuario(id):
            try:
                current_app.logger.info("API -> obtener_eventos_usuario()")
                response = self.eventoService.obtener_eventos_por_usuario(id)
                return Response(response,mimetype='application/json')
            except Exception as e:
                return jsonify({'error':str(e)})

        # Endpoint que recibe la petición para obtener un evento por su id
        @self.api_bp.route('/evento/<id>', methods=['GET'])
        def obtener_evento_por_id(id):
            try:
                current_app.logger.info("API -> obtener_evento_por_id()")
                response = self.eventoService.obtener_evento_por_id(id)
                return Response(response, mimetype='application/json')
            except EventoNotFoundException as e:
                return jsonify({'error':str(e)}),404

        # Endpoint para modificar un evento indicando su id 
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
        
        # Endpoint para eliminar un evento indicando su id
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