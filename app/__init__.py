from flask import Flask
from config import DevelopmentConfig

from flask_login import LoginManager

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "main.login"
    
    # Register blueprints
    from app.main.routes import main as main_bp
    # from .main import bp as main_bp
    app.register_blueprint(main_bp)

    return app