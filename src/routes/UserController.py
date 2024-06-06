#Imports
from flask import request, jsonify, Response, Blueprint, current_app
from src.services.UserService import UserService
from src.services.AuthService import AuthService
from src.models.UserNotFoundException import UserNotFoundException

# Controlador que contiene los Endpoints y el tratamiento de los errores para los usuarios
class UserController():

    # Constructor
    def __init__(self, userService:UserService, authService:AuthService):
        self.api_bp = Blueprint('user', __name__, url_prefix='/api')
        self.userService = userService
        self.authService = authService
        self.init_routes()

    # Método que inicializa todos los Endpoints del controlador
    def init_routes(self):
        #Aquí van los endpoints

        # Endpoint encargado de realizar el login de un usuario en la aplicación
        @self.api_bp.route('/auth/login',methods=['POST'])
        def login():
            try:
                current_app.logger.info("API -> login()")
                body = request.get_json()
                if not body or not isinstance(body,dict):
                    raise Exception("Formato json no valido")
                
                if not all(key in body for key in ('username', 'password')):
                    raise Exception("Falta algún campo")
                
                token, user = self.authService.login(body['username'],body['password'])
                
                response = jsonify({'login':True,'token':token, 'user_id':str(user['_id'])})
                response.headers['Authorization'] = f'{token}'
                return response
            except Exception as e:
                return jsonify({'error':str(e)}),400

        # Endponit encargado de realizar el registro de un nuevo usuario en la aplicación
        @self.api_bp.route('/auth/register',methods=['POST'])
        def register():
            try:
                current_app.logger.info("API -> register()")
                body = request.get_json()
                if not body or not isinstance(body,dict):
                    raise Exception("Formato json no válido")
                
                if not all(key in body for key in ('username','password','email')):
                    raise Exception("Falta algún campo")
                
                self.userService.crear_usuario(body)

                return jsonify({
                    'mensaje':'Registrado correctamente',
                    })
            except Exception as e:
                return jsonify({'error':str(e)}),400

        # Endpoint encargado de crear un nuevo usuario
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

        # Endpoint encargado de cambiar la contraseña de un usuario indicando su id 
        @self.api_bp.route('/user/<id>/changePassword', methods=['PUT'])
        def cambiar_contraseña(id):
            try:
                current_app.logger.info("API -> cambiar_contraseña()")
                body = request.get_json()
                self.authService.changePassword(id,body)
                return jsonify({
                    'mensaje':'Contraseña modificada'
                })
            except Exception as e:
                return jsonify({'error':str(e)}),400

        # Endpoint encargado de obtener todos los usuarios que existen   
        @self.api_bp.route('/users', methods=['GET'])
        def obtener_usuarios():
            current_app.logger.info("API -> obtener_usuarios()")
            response = self.userService.obtener_usuarios()
            return Response(response,mimetype='application/json')

        # Endpoint encargado de obtener un usuario por su id
        @self.api_bp.route('/user/<id>', methods=['GET'])
        def obtener_usuario_por_id(id):
            try:
                current_app.logger.info("API -> obtener_usuario_por_id()")
                response = self.userService.obtener_usuario_por_id(id)
                return Response(response, mimetype='application/json')
            except UserNotFoundException as e:
                return jsonify({'error':str(e)}),404

        # Endpoint encargado de modificar un usuario indicando su id
        @self.api_bp.route('/user/<id>', methods=['PUT'])
        def modificar_usuario(id):
            try:
                current_app.logger.info("API -> modificar_usuario()")
                body = request.get_json()
                self.userService.modificar_usuario(id,body)
                return jsonify({'mensaje':'Usuario modificado'})
            except UserNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        # Endpoint encargado de eliminar un usuario por su id
        @self.api_bp.route('/user/<id>', methods=['DELETE'])
        def eliminar_usuario(id):
            try:
                current_app.logger.info("API -> eliminar_usuario()")
                self.userService.eliminar_usuario(id)
                return jsonify({'mensaje':'Usuario eliminado'})
            except UserNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400
            
        # Endpoint encargado de obtener todas las notas del usuario indicando su id
        @self.api_bp.route('/user/<id>/notas')
        def obtener_notas_por_user(id):
            try:
                current_app.logger.info("API -> obtener_notas_por_user()")
                response = self.userService.obtener_notas_por_user(id)
                return Response(response, mimetype='application/json')
            except UserNotFoundException as e:
                return jsonify({'error':str(e)}),404

        # Endponit encargado de obtener todas las listas de tareas del usuario indicando su id   
        @self.api_bp.route('/user/<user_id>/listaTareas', methods=['GET'])
        def obtener_listaTareas_por_user(user_id):
            try:
                current_app.logger.info("API -> obtener_listaTareas_por_user()")
                response = self.userService.obtener_listasTareas_por_user(user_id)
                return Response(response, mimetype='application/json')
            except UserNotFoundException as e:
                return jsonify({'error':str(e)}),404
            except Exception as e:
                return jsonify({'error':str(e)}),400

        # Endpoint encargado de obtener todas las tareas completadas del usuario. 
        @self.api_bp.route('listaTareas/getCompletedTasks/<user_id>', methods=['GET'])
        def obtener_tareas_completadas(user_id):
            current_app.logger.info("API -> obtener_tareas_completadas()")
            response = self.userService.obtener_tareas_completadas(user_id)
            return Response(response,mimetype='application/json')