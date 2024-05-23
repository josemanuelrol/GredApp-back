#Imports
from flask import request, jsonify, Response, Blueprint, current_app
from src.services.ListaTareasService import ListaTareasService
from src.models.ListaTareasNotFoundException import ListaTareasNotFoundException
from src.models.TareaNotFoundException import TareaNotFoundException

class ListaTareasController():

    def __init__(self, listaTareasService:ListaTareasService):
        self.api_bp = Blueprint('listaTareas', __name__, url_prefix='/api')
        self.listaTareasService = listaTareasService
        self.init_routes()

    def init_routes(self):
        #Aquí van los endpoints

        @self.api_bp.route('/listaTareas', methods=['POST'])
        def crear_listaTareas():
            try:
                current_app.logger.info("API -> crear_listaTareas()")
                body = request.get_json()
                response = self.listaTareasService.crear_listaTareas(body)
                return jsonify({
                    'id':response,
                    'mensaje':'Lista de tareas creada'
                    })
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/listasTareas', methods=['GET'])
        def obtener_listasTareas():
            try:
                current_app.logger.info("API -> obtener_listasTareas()")
                response = self.listaTareasService.obtener_listasTareas()
                return Response(response,mimetype='application/json')
            except Exception as e:
                return jsonify({'error':str(e)}),404
            
        @self.api_bp.route('/listaTareas/<id>', methods=['GET'])
        def obtener_listaTareas_por_id(id):
            try:
                current_app.logger.info("API -> obtener_listaTareas_por_id()")
                response = self.listaTareasService.obtener_listaTareas_por_id(id)
                return Response(response, mimetype='application/json')
            except ListaTareasNotFoundException as e:
                return jsonify({'error':str(e)}),404
            
        @self.api_bp.route('/listaTareas/user/<user_id>', methods=['GET'])
        def obtener_listaTareas_por_user(user_id):
            try:
                current_app.logger.info("API -> obtener_listaTareas_por_user()")
                response = self.listaTareasService.obtener_listasTareas_por_user(user_id)
                return Response(response, mimetype='application/json')
            except ListaTareasNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/listaTareas/<id>', methods=['PUT'])
        def modificar_listaTareas(id):
            try:
                current_app.logger.info("API -> modificar_listaTareas()")
                body = request.get_json()
                self.listaTareasService.modificar_listaTareas(id,body)
                return jsonify({'mensaje':'Lista de tareas modificada'})
            except ListaTareasNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/listaTareas/<id>', methods=['DELETE'])
        def eliminar_listaTareas(id):
            try:
                current_app.logger.info("API -> eliminar_listaTareas()")
                self.listaTareasService.eliminar_listaTareas(id)
                return jsonify({'mensaje':'Lista de tareas eliminada'})
            except ListaTareasNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400

        #TAREAS

        @self.api_bp.route('listaTareas/<id>/getTasks', methods=['GET'])
        def obtener_tareas(id):
            current_app.logger.info("API -> obtener_tareas()")
            response = self.listaTareasService.obtener_tareas(id)
            return Response(response, mimetype='application/json')
            
        @self.api_bp.route('listaTareas/<id>/getTask/<id_task>', methods=['GET'])
        def obtener_tarea_por_id(id,id_task):
            try:
                current_app.logger.info("API -> obtener_tarea_por_id()")
                response = self.listaTareasService.obtener_tarea_por_id(id,id_task)
                return Response(response, mimetype='application/json')
            except Exception as e:
                return jsonify({'error':str(e)}),404

        @self.api_bp.route('/listaTareas/<id>/addTask', methods=['PUT'])
        def aniadir_tarea(id):
            try:
                current_app.logger.info("API -> aniadir_tarea()")
                body = request.get_json()
                self.listaTareasService.aniadir_tarea(id, body)
                return jsonify({'mensaje':'Tarea añadida'})
            except ListaTareasNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/listaTareas/<id>/updateTask/<id_task>', methods=['PUT'])
        def modificar_tarea(id,id_task):
            try:
                current_app.logger.info("API -> modificar_tarea()")
                taskBody = request.get_json()
                self.listaTareasService.modificar_tarea(id,id_task,taskBody)
                return jsonify({'mensaje':'Tarea modificada'})
            except ListaTareasNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except TareaNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        @self.api_bp.route('/listaTareas/<id>/deleteTask/<id_task>', methods=['PUT'])
        def eliminar_tarea(id, id_task):
            try:
                current_app.logger.info("API -> aniadir_tarea()")
                self.listaTareasService.eliminar_tarea(id, id_task)
                return jsonify({'mensaje':'Tarea eliminada'})
            except ListaTareasNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400