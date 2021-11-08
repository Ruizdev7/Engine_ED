class Config:
    DEBUG = True
    TESTING = True


    #CONFIGURACION DE LA BASE DE DATOS SQLALCHEMY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123qweAs*@localhost:3306/dbEngine"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    SECRET_KEY = 'hardsecretkey'
    DEBUG = True
    TESTING = True
