from flask import Flask
import logging
from src.database.UserRepository import UserRepository
from src.database.EventoRepository import EventoRepository
from src.database.NotaRepository import NotaRepository
from src.database.ListaTareasRepository import ListaTareasRepository
from src.services.UserService import UserService
from src.services.NotaService import NotaService
from src.services.EventoService import EventoService
from src.services.ListaTareasService import ListaTareasService
from src.services.AuthService import AuthService
from src.routes.UserController import UserController
from src.routes.NotaController import NotaController
from src.routes.EventoController import EventoController
from src.routes.ListaTareasController import ListaTareasController

# Método que crea y configura la aplicación Flask instanciando los repositorios, servicios y controladores. Además también configura el registro de los logs de la aplicación.
def create_app(config):

    app = Flask(__name__)

    app.config.from_object(config)

    __configure_logging(app,config)

    #Configuramos los repositorios
    userRepository = UserRepository(app)
    notaRepository = NotaRepository(app)
    eventoRepository = EventoRepository(app)
    listaTareasRepository = ListaTareasRepository(app)

    #Configuramos los servicios
    listaTareasService = ListaTareasService(listaTareasRepository)
    userService = UserService(userRepository, listaTareasService, notaRepository, listaTareasRepository)
    notaService = NotaService(notaRepository)
    eventoService = EventoService(eventoRepository,userService)
    authService = AuthService(userService)

    #Configuramos los controladores
    userController = UserController(userService,authService)
    app.register_blueprint(userController.api_bp)
    notaController = NotaController(notaService)
    app.register_blueprint(notaController.api_bp)
    eventoController = EventoController(eventoService)
    app.register_blueprint(eventoController.api_bp)
    listaTareasController = ListaTareasController(listaTareasService)
    app.register_blueprint(listaTareasController.api_bp)
    
    return app

# Método que configura el tratamiento de los logs de la aplicación.
def __configure_logging(app, config):
    
    #Eliminamos los posibles manejadores, si existen, del logger por defecto
    del app.logger.handlers[:]

    #Añadimos el logger por defecto a la lista de loggers
    backLogger = app.logger
    backHandlers = []

    #Creamos un manejador para escribir los mensajes por consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(__verbose_formatter())
    console_handler.setLevel(config.CONSOLE_LOGS_LEVEL)

    if config.CONSOLE_LOGS:
        backHandlers.append(console_handler)

    for handlr in backHandlers:
        backLogger.addHandler(handlr)
    backLogger.propagate = False
    backLogger.setLevel(logging.DEBUG)

def __verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )