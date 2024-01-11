from flask import Flask
from config import DevelopmentConfig

from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

login_manager = LoginManager(app)
login_manager.login_view = "login"

from app import routes