from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize extensions
    db.init_app(app)
    
    # register blueprints, etc…
    return app

