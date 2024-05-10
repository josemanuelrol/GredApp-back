#Imports
import os
from dotenv import load_dotenv
from src.app import create_app
from config import Config, ProductionConfig

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

#Ejecutando aplicación Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=configuration.PORT)