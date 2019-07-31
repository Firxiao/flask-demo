import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xxxx'
    FLASK_ADMIN = os.environ.get('ADMIN')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    TEMPLATES_AUTO_RELOAD = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
