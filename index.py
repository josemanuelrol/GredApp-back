#Imports
import os
from dotenv import load_dotenv
from src.app import create_app
from config import Config, ProductionConfig
from flask import request, jsonify
from src.utils.VerifyToken import VerifyToken

#Cargando variables de entorno de archivo .env
load_dotenv()

env_config = os.getenv("APP_ENV")

#Eligiendo archivo de configuración
if env_config == 'dev':
    configuration = Config()
elif env_config == 'prod':
    configuration = ProductionConfig()

#Creando app Flask
app = create_app(configuration)

verifyToken = VerifyToken()

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, PUT, DELETE'
    if request.method == 'POST':
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
    return response

@app.before_request
def authenticate():
    if request.method != 'OPTIONS':
        if (request.endpoint != 'user.login' and request.endpoint != 'user.crear_usuario') and not verifyToken.verifyToken():
            return jsonify({'error':'Usuario no autorizado'}),401

#Ejecutando aplicación Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=configuration.PORT)