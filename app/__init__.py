from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config: dict = None):
    app = Flask(__name__)
    app.config.from_object(Config)

    # If test_config is passed, override before we bind anything
    if test_config:
        app.config.update(test_config)

    # Now bind the database extension
    db.init_app(app)

    # Register blueprints
    from app.api.matches import bp as matches_bp

    app.register_blueprint(matches_bp)

    return app
