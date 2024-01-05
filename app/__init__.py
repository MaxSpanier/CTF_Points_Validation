from flask import Flask
from config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app