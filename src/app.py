from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from src.database.UserRepository import UserRepository
from src.database.TareaRepository import TareaRepository
from src.database.CalendarioRepository import CalendarioRepository
from src.database.EventoRepository import EventoRepository
from src.database.NotaRepository import NotaRepository
from src.database.ListaTareasRepository import ListaTareasRepository
from src.services.UserService import UserService
from src.services.TareaService import TareaService
from src.services.NotaService import NotaService
from src.services.EventoService import EventoService
from src.services.CalendarioService import CalendarioService
from src.services.ListaTareasService import ListaTareasService
from src.routes.UserController import UserController
from src.routes.TareaController import TareaController
from src.routes.NotaController import NotaController
from src.routes.EventoController import EventoController
from src.routes.CalendarioController import CalendarioController
from src.routes.ListaTareasController import ListaTareasController


def create_app(config):

    app = Flask(__name__)

    app.config.from_object(config)

    __configure_logging(app,config)

    #Configuramos los repositorios
    userRepository = UserRepository(app)
    tareaRepository = TareaRepository(app)
    notaRepository = NotaRepository(app)
    eventoRepository = EventoRepository(app)
    calendarioRepository = CalendarioRepository(app)
    listaTareasRepository = ListaTareasRepository(app)

    #Configuramos los servicios
    userService = UserService(userRepository)
    tareaService = TareaService(tareaRepository)
    notaService = NotaService(notaRepository)
    eventoService = EventoService(eventoRepository)
    calendarioService = CalendarioService(calendarioRepository)
    listaTareasService = ListaTareasService(listaTareasRepository)

    #Configuramos los controladores
    userController = UserController(userService)
    app.register_blueprint(userController.api_bp)
    tareaController = TareaController(tareaService)
    app.register_blueprint(tareaController.api_bp)
    notaController = NotaController(notaService)
    app.register_blueprint(notaController.api_bp)
    eventoController = EventoController(eventoService)
    app.register_blueprint(eventoController.api_bp)
    calendarioController = CalendarioController(calendarioService)
    app.register_blueprint(calendarioController.api_bp)
    listaTareasController = ListaTareasController(listaTareasService)
    app.register_blueprint(listaTareasController.api_bp)
    
    return app

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

    #Creamos un manejador para escribir los mensajes en un archivo
    file_handler = RotatingFileHandler("./src/utils/log/app.log", maxBytes=1024*1024,backupCount=5)
    file_handler.setFormatter(__verbose_formatter())
    file_handler.setLevel(config.FILE_LOGS_LEVEL)

    if config.FILE_LOGS:
        backHandlers.append(file_handler)
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