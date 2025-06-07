from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize extensions
    db.init_app(app)

    # register our matches API
    from app.api.matches import bp as matches_bp
    app.register_blueprint(matches_bp)
    
    return app

