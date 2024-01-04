import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")

class DevelopmentConfig(Config):
    Testing = True
    SECRET_KEY = '\xc5\xde=\xf4Q\x08)\xd0\xfcT\x1d*D\x1aQ\xd3\xb3\x80s\x8b\xc4R\x08\xd8'

class ProductionConfig(Config):
    pass
