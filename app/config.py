import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")

class DevelopmentConfig(Config):
    Testing = True
    SECRET_KEY = '\xc5\xde=\xf4Q\x08)\xd0\xfcT\x1d*D\x1aQ\xd3\xb3\x80s\x8b\xc4R\x08\xd8'

    # AWS_DEFAULT_REGION = "eu-central-1"
    # AWS_COGNITO_DOMAIN = "domain"
    # AWS_COGNITO_USER_POOL_ID = "eu-central-1_5mSUkATcN"
    # AWS_COGNITO_USER_POOL_CLIENT_ID = "je05qrug545nag8g6amgp2j6p"
    # AWS_COGNITO_USER_POOL_CLIENT_SECRET = "1l5657bb1shhs9mfttjrlu6e39l8smr3ii5d81cihjt2v58t94cl"
    # AWS_COGNITO_REDIRECT_URL = "/loggedin"

class ProductionConfig(Config):
    pass
