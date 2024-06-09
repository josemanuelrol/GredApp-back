# Clases con los parámetros de configuración de la aplicación.
class Config(object):
    ENV='development'
    SECRET_KEY='clavesecreta'
    MONGO_URI='databaseURI'
    DEBUG=True
    PORT=5000
    CONSOLE_LOGS=True
    CONSOLE_LOGS_LEVEL="DEBUG"

class ProductionConfig(Config):
    ENV='production'
    MONGO_URI='databaseURI'
    DEBUG=False
    CONSOLE_LOGS=False
    CONSOLE_LOGS_LEVEL="INFO"
