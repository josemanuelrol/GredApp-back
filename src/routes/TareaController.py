#Imports
from flask import request, jsonify, Response, Blueprint, current_app
from src.services.TareaService import TareaService
from src.models.TareaNotFoundException import TareaNotFoundException

class TareaController():

    def __init__(self, tareaService:TareaService):
        self.api_bp = Blueprint('tarea', __name__, url_prefix='/api')
        self.tareaService = tareaService
        self.init_routes()

    def init_routes(self):
        #Aquí van los endpoints

        @self.api_bp.route('/tarea', methods=['POST'])
        def crear_tarea():
            try:
                current_app.logger.info("API -> crear_tarea()")
                body = request.get_json()
                response = self.tareaService.crear_tarea(body)
                return jsonify({
                    'id':response,
                    'mensaje':'Tarea creada'
                    })
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/tareas', methods=['GET'])
        def obtener_tareas():
            current_app.logger.info("API -> obtener_tareas()")
            response = self.tareaService.obtener_tareas()
            return Response(response,mimetype='application/json')
        
        @self.api_bp.route('/tarea/<id>', methods=['GET'])
        def obtener_tarea_por_id(id):
            try:
                current_app.logger.info("API -> obtener_tarea_por_id()")
                response = self.tareaService.obtener_tarea_por_id(id)
                return Response(response, mimetype='application/json')
            except TareaNotFoundException as e:
                return jsonify({'error':str(e)}),404
            
        @self.api_bp.route('/tarea/<id>', methods=['PUT'])
        def modificar_tarea(id):
            try:
                current_app.logger.info("API -> modificar_tarea()")
                body = request.get_json()
                self.tareaService.modificar_tarea(id,body)
                return jsonify({'mensaje':'Tarea modificada'})
            except TareaNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/tarea/<id>', methods=['DELETE'])
        def eliminar_tarea(id):
            try:
                current_app.logger.info("API -> eliminar_tarea()")
                self.tareaService.eliminar_tarea(id)
                return jsonify({'mensaje':'Tarea eliminada'})
            except TareaNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400