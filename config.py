# Clases con los parámetros de configuración de la aplicación.
class Config(object):
    ENV='development'
    SECRET_KEY='3412d9394c2cc785e6e09e053ef0f4d78d86004cf002c1945108640a4b8a303f'
    MONGO_URI='mongodb+srv://user:hum6Vi6lODovK7bY@gredapp.blaorug.mongodb.net/GredApp'
    DEBUG=True
    PORT=5000
    CONSOLE_LOGS=True
    CONSOLE_LOGS_LEVEL="DEBUG"

class ProductionConfig(Config):
    ENV='production'
    MONGO_URI='mongodb+srv://user:hum6Vi6lODovK7bY@gredapp.blaorug.mongodb.net/GredApp'
    DEBUG=False
    CONSOLE_LOGS=False
    CONSOLE_LOGS_LEVEL="INFO"
