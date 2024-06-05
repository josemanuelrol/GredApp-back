class Config(object):
    ENV='development'
    SECRET_KEY='mi_clave_secreta'
    MONGO_URI='mongodb+srv://user:hum6Vi6lODovK7bY@gredapp.blaorug.mongodb.net/GredApp'
    DEBUG=True
    PORT=5000
    CONSOLE_LOGS=True
    CONSOLE_LOGS_LEVEL="DEBUG"
    FILE_LOGS=True
    FILE_LOGS_LEVEL="DEBUG"

class ProductionConfig(Config):
    ENV='production'
    MONGO_URI=''
    DEBUG=False
