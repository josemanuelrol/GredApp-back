class Config(object):
    ENV='development'
    SECRET_KEY='mi_clave_secreta'
    MONGO_URI='mongodb://localhost:27017/gredapp'
    DEBUG=True
    PORT=5000
    APPLICATION_ROOT='/api'
    CONSOLE_LOGS=True
    CONSOLE_LOGS_LEVEL="DEBUG"
    FILE_LOGS=True
    FILE_LOGS_LEVEL="DEBUG"

class ProductionConfig(Config):
    ENV='production'
    MONGO_URI=''
    DEBUG=False
