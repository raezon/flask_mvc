from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Initialize the database (but don't initialize it here)
db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    #app.secret_key = 'zixalTEst'
     # Load configurations from .env
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the Talisman security extension
    # Initialize Flask-Talisman
    talisman = Talisman(
        app,
        content_security_policy={
            "default-src": ["'self'"],
            "style-src": ["'self'", "https://stackpath.bootstrapcdn.com", "https://cdn.jsdelivr.net"],
        },
    )

    # Load configurations
    app.config.from_object("app.config.Config")

    # Initialize plugins
    db.init_app(app)

    # Register blueprints/routes
    from app.controllers import register_blueprints

    register_blueprints(app)

    return app
